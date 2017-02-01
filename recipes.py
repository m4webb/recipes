from PyQt5.QtWidgets import (
        QWidget, QAction, qApp, QListView, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout,
        QAbstractItemView, QCalendarWidget, QTextEdit, QTabWidget
        )
from PyQt5.QtGui import QIcon, QFont, QColor, QTextDocument, QPalette
from PyQt5.QtCore import Qt

import database
import state

SINGLE_DAY_FORMAT = "dddd MMMM dd"

class RecipeApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.mealPlan = state.MealPlan()
        self.initUI()
        self.updateAll()
     
    def initUI(self):
        newFont = QFont("Laksaman", 14) 
        self.setFont(newFont)
        recipesByTag = {}
        recipeList = QListWidget(self)
        for recipe in database.RECIPES:
            for tag in recipe.tags:
                if tag not in recipesByTag:
                    recipesByTag[tag] = []
                recipesByTag[tag].append(recipe)
        for tag in sorted(recipesByTag.keys(), key=database.SORT_TAGS.index):
            recipeList.addItem(QListWidgetItem(tag))
            for recipe in recipesByTag[tag]:
                item = RecipeItem(recipe)
                recipeList.addItem(item)
        recipeList.show()
        recipeList.itemActivated.connect(self.selectRecipe)

        self.calendar = RecipeCalendar(self.mealPlan.meals)
        
        recipeVBox = QVBoxLayout()
        recipeVBox.addWidget(self.calendar, 1)
        recipeVBox.addWidget(recipeList, 2)

        self.selectedRecipeList = QListWidget(self)
        self.selectedRecipeList.show()
        self.selectedRecipeList.itemActivated.connect(self.deselectRecipe)

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

        tabs = QTabWidget()
        tabBuild = QWidget()
        tabView = QWidget()
        tabBuild.setLayout(listHBox)    
        tabView.setLayout(textLayout)

        tabs.addTab(tabBuild, "Build")
        tabs.addTab(tabView, "View")

        layout = QVBoxLayout()
        layout.addWidget(tabs)
        layout.addLayout(buttonHBox)

        self.setLayout(layout)
        
        self.setWindowTitle('Webb Family Recipes')    
        self.showMaximized()

    def selectRecipe(self, recipeItem):
        if type(recipeItem) != RecipeItem:
            return
        date = self.calendar.selectedDate() 
        self.mealPlan.addMeal(recipeItem.recipe, date)
        newDate = date.addDays(1)
        self.calendar.setSelectedDate(newDate)
        self.updateAll()

    def deselectRecipe(self, selectedRecipeItem):
        if type(selectedRecipeItem) != SelectedRecipeItem:
            return 
        self.mealPlan.removeMeal(selectedRecipeItem.recipe, selectedRecipeItem.date)
        self.updateAll()

    def toggleIngredient(self, ingredientItem):
        if type(ingredientItem) != IngredientItem:
            return
        self.mealPlan.toggleIngredientRequired(ingredientItem.ingredient.kind)
        self.updateAll()

    def updateAll(self):
        self.updateMeals()
        self.updateIngredients()
        self.updateCalendar()
        self.updateText()

    def updateMeals(self):
        self.selectedRecipeList.clear()
        for date in sorted(self.mealPlan.meals.keys()):
            self.selectedRecipeList.addItem(QListWidgetItem(date.toString(SINGLE_DAY_FORMAT)))
            for recipe in self.mealPlan.meals[date]:
                self.selectedRecipeList.addItem(SelectedRecipeItem(recipe, date))

    def updateIngredients(self):
        self.ingredientList.clear()
        ingredients = self.mealPlan.getIngredients(skipUnrequired = False)
        for purchase in sorted(ingredients.keys()):
            self.ingredientList.addItem(QListWidgetItem("{}".format(purchase)))
            for store in sorted(ingredients[purchase].keys()):
                self.ingredientList.addItem(QListWidgetItem("    {}".format(store)))
                for section in sorted(ingredients[purchase][store].keys()):
                    self.ingredientList.addItem(QListWidgetItem("        {}".format(section)))
                    for ingredient in sorted(ingredients[purchase][store][section].keys()):
                        ingredient = ingredients[purchase][store][section][ingredient]
                        if ingredient.kind in self.mealPlan.unrequiredIngredientKinds:
                            self.ingredientList.addItem(IngredientItem(ingredient, unrequired=True))
                        else:
                            self.ingredientList.addItem(IngredientItem(ingredient))
                            

    def updateCalendar(self):
        view = self.calendar.findChild(QAbstractItemView)
        view.viewport().update()

    def updateText(self):
        doc = QTextDocument()
        contents = []

        contents.append("Shopping List")
        ingredients = self.mealPlan.getIngredients(skipUnrequired = True)
        for purchase in sorted(ingredients.keys()):
            contents.append("")
            contents.append("    {}".format(purchase))
            for store in sorted(ingredients[purchase].keys()):
                contents.append("")
                contents.append("        {}".format(store))
                for section in sorted(ingredients[purchase][store].keys()):
                    contents.append("            {}".format(section))
                    for ingredient in sorted(ingredients[purchase][store][section].keys()):
                        ingredient = ingredients[purchase][store][section][ingredient]
                        contents.append("                {} {} {}".format(ingredient.name, ingredient.quantity, ingredient.unit))

        contents.append("")
        contents.append("")

        contents.append("Meal Plan")
        for date in sorted(self.mealPlan.meals.keys()):
            contents.append("")
            contents.append("        {}".format(date.toString(SINGLE_DAY_FORMAT)))
            for recipe in self.mealPlan.meals[date]:
                if recipe.url:
                    contents.append("              {} ({})".format(recipe.name, recipe.url))
                else:
                    contents.append("              {}".format(recipe.name))

        doc.setPlainText("\n".join(contents))
        self.text.setDocument(doc)

class RecipeItem(QListWidgetItem):

    def __init__(self, recipe):
        super().__init__("    {}".format(recipe.name))
        self.recipe = recipe

class SelectedRecipeItem(QListWidgetItem):

    def __init__(self, recipe, date):
        super().__init__("    {}".format(recipe.name))
        self.recipe = recipe
        self.date = date

class IngredientItem(QListWidgetItem):

    def __init__(self, ingredient, unrequired=False):
        super().__init__("            {} {} {}".format(ingredient.name, ingredient.quantity, ingredient.unit))
        if unrequired:
            font = self.font()
            font.setStrikeOut(True)
            self.setFont(font)
        self.ingredient = ingredient

class RecipeCalendar(QCalendarWidget):

    def __init__(self, meals):
        super().__init__()
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.meals = meals

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
