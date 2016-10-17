import database

class MealPlan():
    def __init__(self):
        self.meals = {}
        self.unrequiredIngredientKinds = set()

    def resolvePurchase(self, purchase, date):
        if purchase == database.PURCHASE_MONTHLY:
            return "Month of {}".format(date.toString("MMMM"))
        elif purchase == database.PURCHASE_WEEKLY:
            sunday = date
            while sunday.dayOfWeek() != 7:
                sunday = sunday.addDays(-1)
            return "Week starting {}".format(sunday.toString("MMMM dd"))
        elif purchase == database.PURCHASE_DAY_OF:
            return "_Day of {}".format(date.toString("dddd MMMM dd"))
        else:
            raise Exception('Cannot resolve purchase policy "{}"'.format(purchase))

    def getIngredients(self, skipUnrequired=True):
        ingredients = {}
        for date in self.meals:
            for recipe in self.meals[date]:
                for ingredient in recipe.ingredients:
                    if skipUnrequired and ingredient.kind in self.unrequiredIngredientKinds:
                        continue
                    name = ingredient.name
                    quantity = ingredient.quantity
                    section = ingredient.section
                    purchase = self.resolvePurchase(ingredient.purchase, date)
                    store = ingredient.store
                    if purchase not in ingredients:
                        ingredients[purchase] = {}
                    if store not in ingredients[purchase]:
                        ingredients[purchase][store] = {}
                    if section not in ingredients[purchase][store]:
                        ingredients[purchase][store][section] = {}
                    if name not in ingredients[purchase][store][section]:
                        ingredients[purchase][store][section][name] = ingredient
                    else:
                        ingredients[purchase][store][section][name] += ingredient
        return ingredients

    def addMeal(self, recipe, date):
        if date not in self.meals:
            self.meals[date] = []
        self.meals[date].append(recipe)

    def removeMeal(self, recipe, date):
        if date not in self.meals:
            raise Exception("No meal for date {}.".format(date))
        if recipe not in self.meals[date]:
            raise Exception("No meal {} on date {}.".format(recipe, date))
        self.meals[date].remove(recipe)
        if len(self.meals[date]) == 0:
            self.meals.pop(date)

    def toggleIngredientRequired(self, ingredientKind):
        if ingredientKind in self.unrequiredIngredientKinds:
            self.unrequiredIngredientKinds.remove(ingredientKind)
        else:
            self.unrequiredIngredientKinds.add(ingredientKind)
