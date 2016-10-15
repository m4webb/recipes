UNIT_CUPS = "cups"
UNIT_OZ = "oz"
UNIT_CANS = "cans"
UNIT_JARS = "jars"
UNIT_EMPTY = ""

DAY_MONDAY = "Monday"
DAY_TUESDAY = "Tuesday"
DAY_WEDNESDAY = "Wednesday"
DAY_THURSDAY = "Thursday"
DAY_FRIDAY = "Friday"
DAY_SATURDAY = "Saturday"
DAY_SUNDAY = "Sunday"

ING_MOZZARELLA_CHEESE = "mozzarella cheese"
ING_ALFREDO_SAUCE = "alfredo sauce"
ING_PASTA = "pasta"
ING_FLOUR = "flour"

class Ingredient():
    def __init__(self, name = "", amount = 0, unit = UNIT_EMPTY):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __repr__(self):
        return "Ingredient({name} {amount} {unit})".format(name=self.name, amount=self.amount, unit=self.unit)

class Recipe():
    def __init__(self, name = "", days = [], ingredients = []):
        self.name = name
        self.days = days
        self.ingredients = ingredients

    def __repr__(self):
        return "Recipe({name})".format(name=self.name)

RECIPES = [
    Recipe(
        name = "Pizza",
        days = [
            DAY_FRIDAY,
            DAY_SATURDAY,
            DAY_SUNDAY,
            ],
        ingredients = [
            Ingredient(name = ING_FLOUR, amount = 4, unit = UNIT_CUPS),
            Ingredient(name = ING_MOZZARELLA_CHEESE, amount = 8, unit = UNIT_OZ),
            ],
        ),
    Recipe(
        name = "Pasta",
        days = [
            DAY_WEDNESDAY,
            DAY_FRIDAY,
            ],
        ingredients = [
            Ingredient(name = ING_PASTA, amount = 8, unit = UNIT_OZ),
            Ingredient(name = ING_ALFREDO_SAUCE, amount = 1, unit = UNIT_JARS),
            ],
        ),
    ]

RECIPES_INDEX = {r.name : r for r in RECIPES}
