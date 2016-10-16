UNIT_CUPS = "cups"
UNIT_OZ = "oz"
UNIT_CANS = "cans"
UNIT_JARS = "jars"
UNIT_EMPTY = ""

TAG_MONDAY = "Monday"
TAG_TUESDAY = "Tuesday"
TAG_WEDNESDAY = "Wednesday"
TAG_THURSDAY = "Thursday"
TAG_FRIDAY = "Friday"
TAG_SATURDAY = "Saturday"
TAG_SUNDAY = "Sunday"
TAG_SIDE = "Side"

STORE_COSTCO = "Costco"
STORE_WINCO = "Winco"

SEC_GROCERY = "Grocery"
SEC_PRODUCE = "Produce"
SEC_DAIRY = "Dairy"

class Amount():
    def __init__(self, quantity = 0, unit = UNIT_EMPTY):
        self.quantity = quantity
        self.unit = unit

class Ingredient():
    def __init__(self, name = "", store = "Other", section = "Other"):
        self.name = name
        self.store = store
        self.section = section 

    def __repr__(self):
        return "Ingredient({name})".format(name=self.name)

class Recipe():
    def __init__(self, name = "", tags = [], ingredients = []):
        self.name = name
        self.tags = tags
        self.ingredients = ingredients

    def __repr__(self):
        return "Recipe({name})".format(name=self.name)

ING_MOZZARELLA_CHEESE = Ingredient(
    name = "Mozzarella cheese",
    store = STORE_COSTCO,
    section = SEC_DAIRY,
    )

ING_ALFREDO_SAUCE = Ingredient(
    name = "Alfredo sauce",
    )

ING_PASTA = Ingredient(
    name = "Pasta",
    )

ING_FLOUR = Ingredient(
    name = "Flour",
    )

RECIPES = [
    Recipe(
        name = "Pizza",
        tags = [
            TAG_FRIDAY,
            TAG_SATURDAY,
            TAG_SUNDAY,
            TAG_SIDE,
            ],
        ingredients = [
            (ING_FLOUR, Amount(quantity = 4, unit = UNIT_CUPS)),
            (ING_MOZZARELLA_CHEESE, Amount(quantity = 8, unit = UNIT_OZ)),
            ],
        ),
    Recipe(
        name = "Pasta",
        tags = [
            TAG_WEDNESDAY,
            TAG_FRIDAY,
            ],
        ingredients = [
            (ING_MOZZARELLA_CHEESE, Amount(quantity = 8, unit = UNIT_OZ)),
            (ING_ALFREDO_SAUCE, Amount(quantity = 1, unit = UNIT_JARS)),
            ],
        ),
    ]

RECIPES_INDEX = {r.name : r for r in RECIPES}
