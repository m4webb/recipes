UNIT_CUPS = "cups"
UNIT_OZS = "oz"
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

PURCHASE_WEEKLY = "Purchase weekly"
PURCHASE_MONTHLY = "Purchase monthly"

class Amount():
    def __init__(self, quantity = 0, unit = UNIT_EMPTY):
        self.quantity = quantity
        self.unit = unit

class IngredientKind():
    def __init__(self, name = "", store = "Other", section = "Other", unit = UNIT_EMPTY, purchase = PURCHASE_WEEKLY ):
        self.name = name
        self.store = store
        self.section = section 
        self.unit = unit
        self.purchase = purchase

    def __repr__(self):
        return "IngredientKind({name})".format(name=self.name)

    def __call__(self, quantity, unit = None):
        if unit is None:
            unit = self.unit
        return Ingredient(kind = self, quantity = quantity, unit = unit)

class Ingredient():
    def __init__(self, kind = "", quantity = 0, unit = UNIT_EMPTY):
        if unit != kind.unit:
            raise Exception("Ingredient unit {} does not match ingredient unit {}.".format(unit, kind.unit))
        self.kind = kind
        self.name = kind.name
        self.store = kind.store
        self.section = kind.section
        self.purchase = kind.purchase
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return "Ingredient({name} {quantity} {unit})".format(name=self.name, quantity=self.quantity, unit=self.unit)

    def __add__(self, x):
        if self.unit != x.unit:
            raise Exception("Ingredient addition units {} and {} do not match.".format(self.unit, x.unit))
        if self.kind != x.kind:
            raise Exception("Ingredient addition kinds {} and {} do not match.".format(self.kind, x.kind))
        return Ingredient(self.kind, self.quantity + x.quantity, self.unit)

class Recipe():
    def __init__(self, name = "", tags = [], ingredients = []):
        self.name = name
        self.tags = tags
        self.ingredients = ingredients

    def __repr__(self):
        return "Recipe({name})".format(name=self.name)

ING_MOZZARELLA_CHEESE = IngredientKind(
    name = "Mozzarella cheese",
    store = STORE_COSTCO,
    section = SEC_DAIRY,
    purchase = PURCHASE_MONTHLY,
    unit = UNIT_OZS,
    )

ING_ALFREDO_SAUCE = IngredientKind(
    name = "Alfredo sauce",
    purchase = PURCHASE_MONTHLY,
    unit = UNIT_JARS,
    )

ING_PASTA = IngredientKind(
    name = "Pasta",
    unit = UNIT_OZS,
    )

ING_FLOUR = IngredientKind(
    name = "Flour",
    unit = UNIT_CUPS,
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
            ING_FLOUR(4, UNIT_CUPS),
            ING_MOZZARELLA_CHEESE(8, UNIT_OZS)
            ],
        ),
    Recipe(
        name = "Pasta",
        tags = [
            TAG_WEDNESDAY,
            TAG_FRIDAY,
            ],
        ingredients = [
            ING_MOZZARELLA_CHEESE(2, UNIT_OZS),
            ING_ALFREDO_SAUCE(1, UNIT_JARS),
            ],
        ),
    ]

RECIPES_INDEX = {r.name : r for r in RECIPES}
