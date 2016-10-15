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

class RecipeApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
      
    def initUI(self):
        newFont = QFont("Laksaman", 14) 
        self.setFont(newFont)

        recipeList = QListWidget(self)
        for i in range(20):
            item = QListWidgetItem("Recipe {}".format(i))
            recipeList.addItem(item)
        recipeList.show()

        selectedRecipeList = QListWidget(self)
        for i in range(10):
            item = QListWidgetItem("Selected Recipe {}".format(i))
            selectedRecipeList.addItem(item)
        selectedRecipeList.show()

        ingredientList = QListWidget(self)
        for i in range(30):
            item = QListWidgetItem("Ingredient {}".format(i))
            ingredientList.addItem(item)
        ingredientList.show()
        ingredientList.setSelectionMode(QAbstractItemView.ExtendedSelection)
 
 
        listHBox = QHBoxLayout()
        listHBox.addWidget(recipeList)
        listHBox.addWidget(selectedRecipeList)
        listHBox.addWidget(ingredientList)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecipeApp()
    sys.exit(app.exec_()) 
