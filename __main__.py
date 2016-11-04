import sys

from PyQt5.QtWidgets import QApplication

import recipes

app = QApplication(sys.argv)
recipeApp = recipes.RecipeApp()
sys.exit(app.exec_()) 
