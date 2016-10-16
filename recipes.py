#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a menubar. The
menubar has one menu with an exit action.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (
        QWidget, QAction, qApp, QApplication, QListView, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout,
        QAbstractItemView, QCalendarWidget, QTextEdit, QTabWidget
        )
from PyQt5.QtGui import QIcon, QFont, QColor, QTextDocument, QPalette
from PyQt5.QtCore import Qt

import database

class RecipeApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.meals = {}
        self.unrequiredIngredients = set()
        self.initUI()
     
    def initUI(self):
        newFont = QFont("Laksaman", 14) 
        self.setFont(newFont)
        recipesByTag = {}
        self.recipeList = QListWidget(self)
        for recipe in database.RECIPES:
            for tag in recipe.tags:
                if tag not in recipesByTag:
                    recipesByTag[tag] = []
                recipesByTag[tag].append(recipe)
        for tag in sorted(recipesByTag.keys()):
            self.recipeList.addItem(QListWidgetItem(tag))
            for recipe in recipesByTag[tag]:
                item = RecipeItem(recipe)
                self.recipeList.addItem(item)
        self.recipeList.show()
        self.recipeList.itemActivated.connect(self.selectRecipe)

        self.calendar = RecipeCalendar(self.meals)
        
        recipeVBox = QVBoxLayout()
        recipeVBox.addWidget(self.calendar, 1)
        recipeVBox.addWidget(self.recipeList, 2)

        self.selectedRecipeList = QListWidget(self)
        self.selectedRecipeList.show()
        self.selectedRecipeList.itemActivated.connect(self.deselectRecipe)
        #self.selectedRecipeList.setDragDropMode(self.selectedRecipeList.InternalMove)

        self.ingredientList = QListWidget(self)
        self.ingredientList.show()
        self.ingredientList.itemActivated.connect(self.toggleIngredient)
 
        listHBox = QHBoxLayout()
        listHBox.addLayout(recipeVBox)
        listHBox.addWidget(self.selectedRecipeList)
        listHBox.addWidget(self.ingredientList)

        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(self.close)

        buttonHBox = QHBoxLayout()
        buttonHBox.addStretch(1)
        buttonHBox.addWidget(quitButton)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        textLayout = QVBoxLayout()
        textLayout.addWidget(self.text)

        self.tabs = QTabWidget()
        tabBuild = QWidget()
        tabView = QWidget()
        tabBuild.setLayout(listHBox)    
        tabView.setLayout(textLayout)

        self.tabs.addTab(tabBuild, "Build")
        self.tabs.addTab(tabView, "View")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.layout.addLayout(buttonHBox)

        self.setLayout(self.layout)
        
        self.setWindowTitle('Webb Family Recipes')    
        self.showMaximized()

    def selectRecipe(self, recipeItem):
        if type(recipeItem) != RecipeItem:
            return
        date = self.calendar.selectedDate() 
        if date not in self.meals:
            self.meals[date] = []
        newDate = date.addDays(1)
        self.calendar.setSelectedDate(newDate)
        self.meals[date].append(recipeItem.recipe)
        self.updateMeals()
        self.updateIngredients()
        self.updateCalendar()
        self.updateText()

    def deselectRecipe(self, recipeItem):
        if type(recipeItem) != SelectedRecipeItem:
            return 
        self.meals[recipeItem.date].remove(recipeItem.recipe)
        if len(self.meals[recipeItem.date]) == 0:
            self.meals.pop(recipeItem.date) 
        self.updateMeals()
        self.updateIngredients()
        self.updateCalendar()
        self.updateText()

    def toggleIngredient(self, ingredientItem):
        if type(ingredientItem) != IngredientItem:
            return
        ingredientItem.toggle()
        self.updateMeals()
        self.updateIngredients()
        self.updateCalendar()
        self.updateText()

    def updateMeals(self):
        self.selectedRecipeList.clear()
        for date in sorted(self.meals.keys()):
            self.selectedRecipeList.addItem(QListWidgetItem(date.toString()))
            for recipe in self.meals[date]:
                self.selectedRecipeList.addItem(SelectedRecipeItem(recipe, date))

    def updateIngredients(self):
        self.ingredientList.clear()
        ingredients = self.getIngredients()
        for location in sorted(ingredients.keys()):
            self.ingredientList.addItem(QListWidgetItem(location))
            for ingredient in sorted(ingredients[location].keys()):
                quantities = [quantity for unit, quantity in ingredients[location][ingredient].items()]
                units = [unit for unit, quantity in ingredients[location][ingredient].items()]
                self.ingredientList.addItem(IngredientItem(ingredient, quantities, units, self.unrequiredIngredients))

    def getIngredients(self):
        ingredients = {}
        for date in self.meals:
            for recipe in self.meals[date]:
                for (ingredient, amount) in recipe.ingredients:
                    name = ingredient.name
                    quantity = amount.quantity
                    unit = amount.unit
                    location = "{} - {}".format(ingredient.store, ingredient.section)
                    if location not in ingredients:
                        ingredients[location] = {}
                    if name not in ingredients[location]:
                        ingredients[location][name] = {}
                    if unit not in ingredients[location][name]:
                        ingredients[location][name][unit] = 0
                    ingredients[location][name][unit] += quantity
        return ingredients

    def updateCalendar(self):
        view = self.calendar.findChild(QAbstractItemView)
        view.viewport().update()

    def updateText(self):
        doc = QTextDocument()
        contents = []

        contents.append("Shopping List")
        prevType = IngredientItem
        for ingredientItemIndex in range(self.ingredientList.count()):
            ingredientItem = self.ingredientList.item(ingredientItemIndex)
            if type(ingredientItem) == IngredientItem and ingredientItem.ingredient in self.unrequiredIngredients:
                continue
            if type(ingredientItem) != IngredientItem and prevType != IngredientItem:
                contents.pop()
            elif type(ingredientItem) != IngredientItem:
                contents.append("")
            contents.append("    {}".format(ingredientItem.text()))
            prevType = type(ingredientItem)
        if prevType != IngredientItem:
            contents.pop()
            contents.pop()

        contents.append("")
        contents.append("")

        contents.append("Meal Plan")
        for date in sorted(self.meals.keys()):
            contents.append("")
            contents.append("    {}".format(date.toString()))
            for recipe in self.meals[date]:
                contents.append("        {}".format(recipe.name))

        doc.setPlainText("\n".join(contents))
        self.text.setDocument(doc)

    def listPopup(self):
        self.text = QTextEdit()
        self.text.show()

class RecipeItem(QListWidgetItem):

    def __init__(self, recipe):
        super().__init__("    {}".format(recipe.name))
        self.recipe = recipe

    def copy(self):
        return RecipeItem(self.name, self.day)

class SelectedRecipeItem(QListWidgetItem):

    def __init__(self, recipe, date):
        super().__init__("    {}".format(recipe.name))
        self.recipe = recipe
        self.date = date

class IngredientItem(QListWidgetItem):

    def __init__(self, ingredient, quantities, units, unrequiredIngredients):
        super().__init__()
        self.ingredient = ingredient
        self.quantities = quantities
        self.units = units
        self.unrequiredIngredients = unrequiredIngredients
        self.resetText()

    def toggle(self):
        if self.ingredient in self.unrequiredIngredients:
            self.unrequiredIngredients.remove(self.ingredient)
        else:
            self.unrequiredIngredients.add(self.ingredient)
        self.resetText()

    def resetText(self):
        if self.ingredient in self.unrequiredIngredients:
            font = self.font()
            font.setStrikeOut(True)
            self.setFont(font)
        unitString = ", ".join(["{} {}".format(quantity, unit) for unit, quantity in zip(self.units, self.quantities)])
        text = "    {} {}".format(self.ingredient, unitString)
        super().setText(text)

class RecipeCalendar(QCalendarWidget):

    def __init__(self, meals):
        super().__init__()
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.meals = meals
        #self.setNavigationBarVisible(False)
        #self.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)

    def paintCell(self, painter, rect, date):
        painter.save()
        if date in self.meals:
            count = len(self.meals[date])
        else:
            count = 0 
        if count == 0:
            painter.fillRect(rect, QColor(255, 255, 255))
        else:
            painter.fillRect(rect, QColor(200, 200, 200))
        if date == self.selectedDate():
            font = painter.font()
            font.setBold(True)
            font.setPointSize(32)
            painter.setFont(font)
        painter.drawText(rect, Qt.AlignCenter, "{}".format(date.day()))
        painter.restore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecipeApp()
    sys.exit(app.exec_()) 
