UNIT_CUPS = "cups"
UNIT_OZS = "oz"
UNIT_CANS = "cans"
UNIT_JARS = "jars"
UNIT_LOAVES = "loaves"
UNIT_TBSPS = "tbsps"
UNIT_TSPS = "tsps"
UNIT_CLOVES = "cloves"
UNIT_EMPTY = ""
UNIT_LBS = "lbs"

TAG_MONDAY = "Monday"
TAG_TUESDAY = "Tuesday"
TAG_WEDNESDAY = "Wednesday"
TAG_THURSDAY = "Thursday"
TAG_FRIDAY = "Friday"
TAG_SATURDAY = "Saturday"
TAG_SUNDAY = "Sunday"
TAG_SIDE = "Side"
TAG_EASY = "Easy"
TAG_FUN = "Fun"
TAG_GUESTS = "Guests"

STORE_COSTCO = "Costco"
STORE_WINCO = "Winco"
STORE_HARMONS = "Harmons"
STORE_GROCERY = "Grocery"

SECTION_GROCERY = "Grocery"
SECTION_PRODUCE = "Produce"
SECTION_DAIRY = "Dairy"
SECTION_BAKERY = "Bakery"
SECTION_BAKING = "Baking"
SECTION_BULK = "Bulk"
SECTION_FROZEN = "Frozen"

PURCHASE_WEEKLY = "Purchase weekly"
PURCHASE_MONTHLY = "Purchase monthly"
PURCHASE_DAY_OF = "Purchase day of"

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
    def __init__(self, name = "", tags = [], ingredients = [], url = ""):
        self.name = name
        self.tags = tags
        self.ingredients = ingredients
        self.url = url

    def __repr__(self):
        return "Recipe({name})".format(name=self.name)

ING_CHEESE_MOZZARELLA = IngredientKind(
    name = "Mozzarella cheese",
    store = STORE_COSTCO,
    section = SECTION_DAIRY,
    unit = UNIT_OZS,
    purchase = PURCHASE_MONTHLY,
    )

ING_ALFREDO_SAUCE = IngredientKind(
    name = "Alfredo sauce",
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    unit = UNIT_JARS,
    purchase = PURCHASE_MONTHLY,
    )

ING_PASTA = IngredientKind(
    name = "Pasta",
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    unit = UNIT_OZS,
    purchase = PURCHASE_MONTHLY,
    )

ING_FLOUR = IngredientKind(
    name = "Flour",
    store = STORE_WINCO,
    section = SECTION_BAKING,
    unit = UNIT_CUPS,
    purchase = PURCHASE_MONTHLY,
    )

ING_FRESH_BREAD = IngredientKind(
    name = "Fresh bread",
    unit = UNIT_LOAVES,
    store = STORE_HARMONS,
    section = SECTION_BAKERY,
    purchase = PURCHASE_DAY_OF,
    )

ING_FRESH_BASIL = IngredientKind(
    name = "Fresh basil",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_DICED_TOMATOES = IngredientKind(
    name = "Crushed tomatoes",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_TOMATO_PASTE = IngredientKind(
    name = "Tomato Paste",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_BASIL = IngredientKind(
    name = "Basil",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_OREGANO = IngredientKind(
    name = "Oregano",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_RED_WINE_VINEGAR = IngredientKind(
    name = "Red wine vingegar",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_MUSHROOMS = IngredientKind(
    name = "Mushrooms",
    unit = UNIT_LBS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_CHICKPEAS = IngredientKind(
    name = "Chickpeas",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_BELL_PEPPERS = IngredientKind(
    name = "Bell peppers",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_YELLOW_ONIONS = IngredientKind(
    name = "Yellow onions",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    ) 

ING_AVOCADOS = IngredientKind(
    name = "Avocado",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_OLIVE_OIL = IngredientKind(
    name = "Olive oil",
    unit = UNIT_TBSPS,
    store = STORE_COSTCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_TORTILLAS = IngredientKind(
    name = "Tortillas",
    unit = UNIT_EMPTY,
    store = STORE_COSTCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_RAW_CASHEWS = IngredientKind(
    name = "Raw cashews",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_CILANTRO = IngredientKind(
    name = "Cilantro",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_LIMES = IngredientKind(
    name = "Limes",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_GARLIC_POWDER = IngredientKind(
    name = "Garlic powder",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_CAYENNE_PEPPER = IngredientKind(
    name = "Cayenne pepper",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_RED_ONIONS = IngredientKind(
    name = "Red onions",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_FROZEN_CORN = IngredientKind(
    name = "Frozen corn",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_FROZEN,
    purchase = PURCHASE_MONTHLY,
    )

ING_BLACK_BEANS = IngredientKind(
    name = "Black beans",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_FIRE_ROASTED_DICED_TOMATOES = IngredientKind(
    name = "Fire roasted diced tomatoes",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_BARLEY = IngredientKind(
    name = "Barley",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_VEGETABLE_STOCK = IngredientKind(
    name = "Vegetable stock",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_CUMIN = IngredientKind(
    name = "Cumin",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_SMOKED_PAPRIKA = IngredientKind(
    name = "Smoked Paprika",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_GREEK_YOGURT = IngredientKind(
    name = "Greek yogurt",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_DAIRY,
    purchase = PURCHASE_MONTHLY,
    )

ING_CHIPOTLE_PEPPERS_IN_ADOBO_SAUCE = IngredientKind(
    name = "Chipotle peppers in adobo sauce",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_CHEESE_FETA = IngredientKind(
    name = "Feta cheese",
    unit = UNIT_OZS,
    store = STORE_COSTCO,
    section = SECTION_DAIRY,
    purchase = PURCHASE_MONTHLY,
    )

ING_YEAST = IngredientKind(
    name = "Yeast",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_MAYONNAISE = IngredientKind(
    name = "Mayonnaise",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_GARLIC = IngredientKind(
    name = "Garlic",
    unit = UNIT_CLOVES,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_LEMON = IngredientKind(
    name = "Lemon",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section= SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_ZUCCHINI = IngredientKind(
    name = "Zucchini",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_YELLOW_SQUASH = IngredientKind(
    name = "Yellow squash",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_VEGGIE_BURGERS = IngredientKind(
    name = "Veggie burgers",
    unit = UNIT_EMPTY,
    store = STORE_COSTCO,
    section = SECTION_FROZEN,
    purchase = PURCHASE_MONTHLY,
    )

ING_BURGER_BUNS = IngredientKind(
    name = "Burger buns",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_GREEN_LEAF_LETTUCE = IngredientKind(
    name = "Green leaf lettuce",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_SWEET_POTATOES = IngredientKind(
    name = "Sweet potatoes",
    unit = UNIT_LBS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_HUMMUS = IngredientKind(
    name = "Hummus",
    unit = UNIT_OZS,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_WRAPS = IngredientKind(
    name = "Wraps",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_SPINACH = IngredientKind(
    name = "Spinach",
    unit = UNIT_CUPS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_ONION = IngredientKind(
    name = "Onion",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_BROWN_RICE = IngredientKind(
    name = "Brown rice",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_CHILI_POWDER = IngredientKind(
    name = "Chili powder",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_SALSA = IngredientKind(
    name = "Salsa",
    unit = UNIT_CUPS,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_SHREDDED_LETTUCE = IngredientKind(
    name = "Shredded lettuce",
    unit = UNIT_CUPS,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_CHEESE_PEPPER_JACK = IngredientKind(
    name = "Cheese pepper Jack",
    unit = UNIT_OZS,
    store = STORE_GROCERY,
    section = SECTION_DAIRY,
    purchase = PURCHASE_WEEKLY,
    )

ING_TORTILLA_CHIPS = IngredientKind(
    name = "Tortilla chips",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

RECIPES = [
    Recipe(
        name = "Vegetarian Taco Salad",
        url = "http://www.eatingwell.com/recipe/250064/vegetarian-taco-salad/",
        tags = [
            TAG_MONDAY,
            ],
        ingredients = [
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_ONION(1),
            ING_FROZEN_CORN(1.5, UNIT_CUPS),
            ING_BROWN_RICE(0.75, UNIT_CUPS),
            ING_BLACK_BEANS(1, UNIT_CANS),
            ING_CHILI_POWDER(1, UNIT_TBSPS),
            ING_OREGANO(0.5, UNIT_TBSPS),
            ING_CILANTRO(1),
            ING_SALSA(1, UNIT_CUPS),
            ING_SHREDDED_LETTUCE(2, UNIT_CUPS),
            ING_CHEESE_PEPPER_JACK(4, UNIT_OZS),
            ING_TORTILLA_CHIPS(1),
            ING_LIMES(1),
            ],
    ),
    Recipe(
        name = "Pizza",
        tags = [
            TAG_FRIDAY,
            TAG_SATURDAY,
            TAG_SUNDAY,
            TAG_FUN,
            TAG_GUESTS,
            ],
        ingredients = [
            ING_FLOUR(4, UNIT_CUPS),
            ING_CHEESE_MOZZARELLA(16, UNIT_OZS),
            ING_FRESH_BASIL(1),
            ING_DICED_TOMATOES(1, UNIT_CANS),
            ING_TOMATO_PASTE(1, UNIT_CANS),
            ING_BASIL(1, UNIT_TBSPS),
            ING_OREGANO(0.5, UNIT_TBSPS),
            ING_RED_WINE_VINEGAR(0.1, UNIT_CUPS),
            ING_MUSHROOMS(1, UNIT_LBS),
            ING_YEAST(1, UNIT_TBSPS),
            ],
        ),
    Recipe(
        name = "Roasted Chickpea Fajitas with Cilantro Cashew Crema",
        url = "http://www.makingthymeforhealth.com/roasted-chickpea-fajitas-with-cilantro-cashew-crema/",
        tags = [
            TAG_TUESDAY,
            TAG_GUESTS,
            TAG_FUN,
            ],
        ingredients = [
            ING_CHICKPEAS(1, UNIT_CANS),
            ING_BELL_PEPPERS(2),
            ING_YELLOW_ONIONS(1),
            ING_AVOCADOS(1),
            ING_OLIVE_OIL(3, UNIT_TBSPS),
            ING_TORTILLAS(6),
            ING_RAW_CASHEWS(1, UNIT_CUPS),
            ING_CILANTRO(1),
            ING_LIMES(2),
            ING_GARLIC_POWDER(0.25, UNIT_TSPS),
            ING_CAYENNE_PEPPER(0.25, UNIT_TSPS),
            ],
        ),
    Recipe(
        name = "Crockpot Barley and Bean Tacos with Avocado Chipotle Cream",
        url = "http://potluck.ohmyveggies.com/crockpot-barley-bean-tacos-avocado-chipotle-cream/",
        tags = [
            TAG_TUESDAY,
            TAG_GUESTS,
            TAG_FUN,
            ],
        ingredients = [
            ING_RED_ONIONS(1),
            ING_FROZEN_CORN(1, UNIT_CUPS),
            ING_BLACK_BEANS(1, UNIT_CANS),
            ING_FIRE_ROASTED_DICED_TOMATOES(1, UNIT_CANS),
            ING_BARLEY(1, UNIT_CUPS),
            ING_VEGETABLE_STOCK(2, UNIT_CUPS),
            ING_LIMES(1),
            ING_CUMIN(1, UNIT_TSPS),
            ING_SMOKED_PAPRIKA(0.5, UNIT_TSPS),
            ING_GARLIC_POWDER(0.5, UNIT_TSPS),
            ING_AVOCADOS(1),
            ING_GREEK_YOGURT(2.5, UNIT_TBSPS),
            ING_CHIPOTLE_PEPPERS_IN_ADOBO_SAUCE(1, UNIT_TSPS),
            ING_CHEESE_FETA(4, UNIT_OZS),
            ING_TORTILLAS(6),
            ],
        ),
    Recipe(
        name = "California Grilled Sandwiches",
        tags = [
            TAG_WEDNESDAY,
            ],
        ingredients = [
            ING_MAYONNAISE(0.25, UNIT_CUPS),
            ING_GARLIC(3, UNIT_CLOVES),
            ING_LEMON(1),
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_BELL_PEPPERS(1),
            ING_ZUCCHINI(1),
            ING_RED_ONIONS(1),
            ING_YELLOW_SQUASH(1),
            ING_FRESH_BREAD(1, UNIT_LOAVES),
            ING_CHEESE_FETA(4, UNIT_OZS),
            ],
        ),
    Recipe(
        name = "Classic Veggie Burgers",
        tags = [
            TAG_WEDNESDAY,
            ],
        ingredients = [
            ING_VEGGIE_BURGERS(4),
            ING_AVOCADOS(1),
            ING_RED_ONIONS(0.5),
            ING_MAYONNAISE(0.5, UNIT_CUPS),
            ING_BURGER_BUNS(4),
            ING_GREEN_LEAF_LETTUCE(1),
            ],
        ),
    Recipe(
        name = "Hummus Wraps",
        tags = [
            TAG_WEDNESDAY,
            ],
        ingredients = [
            ING_HUMMUS(10, UNIT_OZS),
            ING_WRAPS(4),
            ING_CHEESE_FETA(4, UNIT_OZS),
            ING_BELL_PEPPERS(1),
            ING_SPINACH(2, UNIT_CUPS),
            ING_RED_ONIONS(0.5),
            ],
        ),
    Recipe(
        name = "Sweet Potato Fries",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_SWEET_POTATOES(1, UNIT_LBS),
            ],
        ),
    Recipe(
        name = "Fresh Bread",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_FRESH_BREAD(1, UNIT_LOAVES),
            ],
        ),
    Recipe(
        name = "Leftovers",
        tags = [
            TAG_EASY,
            ],
        ingredients = [
            ],
        ),
    ]

RECIPES_INDEX = {r.name : r for r in RECIPES}
