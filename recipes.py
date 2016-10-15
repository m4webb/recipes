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

from database import recipes

class RecipeApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
      
    def initUI(self):
        newFont = QFont("Laksaman", 14) 
        self.setFont(newFont)

        self.recipeList = QListWidget(self)
        for recipe in recipes:
            item = RecipeItem(recipe)
            self.recipeList.addItem(item)
        self.recipeList.show()
        self.recipeList.itemActivated.connect(self.selectRecipe)

        self.selectedRecipeList = QListWidget(self)
        self.selectedRecipeList.show()
        self.selectedRecipeList.itemActivated.connect(self.deselectRecipe)

        self.ingredientList = QListWidget(self)
        self.ingredientList.show()
 
        listHBox = QHBoxLayout()
        listHBox.addWidget(self.recipeList)
        listHBox.addWidget(self.selectedRecipeList)
        listHBox.addWidget(self.ingredientList)

        makeButton = QPushButton("Make")
        quitButton = QPushButton("Quit")
 
        buttonHBox = QHBoxLayout()
        buttonHBox.addStretch(1)
        buttonHBox.addWidget(makeButton)
        buttonHBox.addWidget(quitButton)

        vbox = QVBoxLayout()
        vbox.addLayout(listHBox)
        vbox.addLayout(buttonHBox)
        
        self.setLayout(vbox)    
        
        self.setWindowTitle('Webb Family Recipes')    
        self.show()

    def selectRecipe(self, recipe):
        self.selectedRecipeList.addItem(recipe.copy())
        self.updateIngredients()

    def deselectRecipe(self, recipe):
        self.selectedRecipeList.takeItem(self.selectedRecipeList.row(recipe))
        self.updateIngredients()

    def updateIngredients(self):
        self.ingredientList.clear()
        for recipeIndex in range(self.selectedRecipeList.count()):
            recipe = self.selectedRecipeList.item(recipeIndex)
            for ingredient in recipe.ingredients:
                self.ingredientList.addItem(QListWidgetItem(str(ingredient)))

class RecipeItem(QListWidgetItem):

    def __init__(self, name):
        super().__init__(name)
        if name not in recipes:
            raise Exception("Recipe {} not found!".format(name))
        self.name = name
        self.ingredients = recipes[name]

    def copy(self):
        return RecipeItem(self.name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecipeApp()
    sys.exit(app.exec_()) 
