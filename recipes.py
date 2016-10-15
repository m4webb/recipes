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
        QAbstractItemView,
        )
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

import database

class RecipeApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
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
        self.selectedRecipeList.setDragDropMode(self.selectedRecipeList.InternalMove)

        self.ingredientList = QListWidget(self)
        self.ingredientList.show()
 
        listHBox = QHBoxLayout()
        listHBox.addWidget(self.recipeList)
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
        self.selectedRecipeList.addItem(recipe.copy())
        self.updateIngredients()

    def deselectRecipe(self, recipe):
        self.selectedRecipeList.takeItem(self.selectedRecipeList.row(recipe))
        self.updateIngredients()

    def updateIngredients(self):
        self.ingredientList.clear()
        ingredients = {}
        for recipeIndex in range(self.selectedRecipeList.count()):
            recipe = self.selectedRecipeList.item(recipeIndex)
            for ingredient in recipe.ingredients:
                name, amount, unit = ingredient.name, ingredient.amount, ingredient.unit
                if name not in ingredients:
                    ingredients[name] = {}
                if unit not in ingredients[name]:
                    ingredients[name][unit] = 0
                ingredients[name][unit] += amount
        for ingredient in ingredients:
            unitString = ", ".join("{} {}".format(amount, unit) for unit, amount in ingredients[ingredient].items())
            self.ingredientList.addItem( QListWidgetItem("{} {}".format(ingredient, unitString)))

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecipeApp()
    sys.exit(app.exec_()) 
