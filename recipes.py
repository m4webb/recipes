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
        QAbstractItemView, QCalendarWidget
        )
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import Qt

import database

class RecipeApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.meals = {}
        self.initUI()

     
    def initUI(self):
        newFont = QFont("Laksaman", 14) 
        self.setFont(newFont)

        self.recipeList = QListWidget(self)
        for recipe in database.RECIPES:
            for day in recipe.days:
                item = RecipeItem(recipe.name, day)
                self.recipeList.addItem(item)
        self.recipeList.show()
        self.recipeList.itemActivated.connect(self.selectRecipe)

        self.selectedRecipeList = QListWidget(self)
        self.selectedRecipeList.show()
        self.selectedRecipeList.itemActivated.connect(self.deselectRecipe)
        #self.selectedRecipeList.setDragDropMode(self.selectedRecipeList.InternalMove)

        self.ingredientList = QListWidget(self)
        self.ingredientList.show()
 
        self.calendar = RecipeCalendar(self.meals)

        listHBox = QHBoxLayout()
        listHBox.addWidget(self.recipeList)
        listHBox.addWidget(self.calendar)
        listHBox.addWidget(self.selectedRecipeList)
        listHBox.addWidget(self.ingredientList)

        makeButton = QPushButton("Make")
        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(self.close)

        buttonHBox = QHBoxLayout()
        buttonHBox.addStretch(1)
        buttonHBox.addWidget(makeButton)
        buttonHBox.addWidget(quitButton)

        vbox = QVBoxLayout()
        vbox.addLayout(listHBox)
        vbox.addLayout(buttonHBox)
        
        self.setLayout(vbox)    
        
        self.setWindowTitle('Webb Family Recipes')    
        self.showMaximized()

    def selectRecipe(self, recipe):
        date = self.calendar.selectedDate() 
        if date not in self.meals:
            self.meals[date] = []
        self.meals[date].append(recipe)
        self.updateMeals()
        self.updateIngredients()
        self.updateCalendar()

    def deselectRecipe(self, recipeItem):
        if type(recipeItem) != SelectedRecipeItem:
            return 
        self.meals[recipeItem.date].remove(recipeItem.recipe)
        if len(self.meals[recipeItem.date]) == 0:
            self.meals.pop(recipeItem.date) 
        self.updateMeals()
        self.updateIngredients()
        self.updateCalendar()

    def updateMeals(self):
        self.selectedRecipeList.clear()
        for date in sorted(self.meals.keys()):
            self.selectedRecipeList.addItem(QListWidgetItem(date.toString()))
            for recipe in self.meals[date]:
                self.selectedRecipeList.addItem(SelectedRecipeItem(recipe, date))

    def updateIngredients(self):
        self.ingredientList.clear()
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
        for location in ingredients:
            self.ingredientList.addItem(QListWidgetItem(location))
            for ingredient in ingredients[location]:
                unitString = ", ".join("{} {}".format(quantity, unit) for unit, quantity
                        in ingredients[location][ingredient].items())
                self.ingredientList.addItem( QListWidgetItem("    {} {}".format(ingredient, unitString)))

    def updateCalendar(self):
        view = self.calendar.findChild(QAbstractItemView)
        view.viewport().update()

class RecipeItem(QListWidgetItem):

    def __init__(self, name, day):
        super().__init__("{} - {}".format(day, name))
        if name not in database.RECIPES_INDEX:
            raise Exception("Recipe {} not found.".format(name))
        recipe = database.RECIPES_INDEX[name]
        if day not in recipe.days:
            raise Exception("Recipe {} not valid for day {}.".format(name, day))
        self.name = name
        self.day = day
        self.ingredients = recipe.ingredients

    def copy(self):
        return RecipeItem(self.name, self.day)

class SelectedRecipeItem(QListWidgetItem):

    def __init__(self, recipe, date):
        super().__init__("    {}".format(recipe.name))
        self.recipe = recipe
        self.date = date

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
            painter.fillRect(rect, QColor(150, 150, 150))
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
