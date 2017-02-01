UNIT_CUPS = "cups"
UNIT_OZS = "oz"
UNIT_CANS = "cans"
UNIT_JARS = "jars"
UNIT_LOAVES = "loaves"
UNIT_TBSPS = "tbsps"
UNIT_TSPS = "tsps"
UNIT_CLOVES = "cloves"
UNIT_LBS = "lbs"
UNIT_SLICES = "slices"
UNIT_EMPTY = ""
UNIT_SERVINGS = "servings"
UNIT_PACKAGES = "packages"

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
TAG_CIRCUMSTANCES = "Circumstances"
TAG_SOUPS = "Soups"
TAG_FISH = "Fish"

SORT_TAGS = [
    TAG_MONDAY,
    TAG_TUESDAY,
    TAG_WEDNESDAY,
    TAG_THURSDAY,
    TAG_FRIDAY,
    TAG_SATURDAY,
    TAG_SUNDAY,
    TAG_CIRCUMSTANCES,
    TAG_SIDE,
    TAG_SOUPS,
    TAG_FISH,
    TAG_GUESTS,
    TAG_FUN,
    TAG_EASY,
    ]

STORE_COSTCO = "Costco"
STORE_WINCO = "Winco"
STORE_HARMONS = "Harmons"
STORE_GROCERY = "Grocery"
STORE_SPECIALTY = "Specialty"

SECTION_GROCERY = "Grocery"
SECTION_PRODUCE = "Produce"
SECTION_DAIRY = "Dairy"
SECTION_BAKERY = "Bakery"
SECTION_BAKING = "Baking"
SECTION_BULK = "Bulk"
SECTION_FROZEN = "Frozen"
SECTION_SPECIALTY = "Specialty"
SECTION_ASIAN = "Asian"

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
    unit = UNIT_TBSPS,
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

ING_PAPRIKA = IngredientKind(
    name = "Paprika",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_SMOKED_PAPRIKA = IngredientKind(
    name = "Smoked paprika",
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
    unit = UNIT_TBSPS,
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

ING_LEMONS = IngredientKind(
    name = "Lemons",
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

ING_ONIONS = IngredientKind(
    name = "Onions",
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

ING_PATO = IngredientKind(
    name = "Pato",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_BUTTER = IngredientKind(
    name = "Butter",
    unit = UNIT_TBSPS,
    store = STORE_COSTCO,
    section = SECTION_DAIRY,
    purchase = PURCHASE_MONTHLY,
    )

ING_SLICED_BREAD = IngredientKind(
    name = "Sliced bread",
    unit = UNIT_SLICES,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_CHEESE = IngredientKind(
    name = "Cheese",
    unit = UNIT_OZS,
    store = STORE_GROCERY,
    section = SECTION_DAIRY,
    purchase = PURCHASE_WEEKLY,
    )

ING_SOBA_NOODLES = IngredientKind(
    name = "Soba noodles",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_MONTHLY,
    )

ING_FROZEN_EDAMAME = IngredientKind(
    name = "Frozen edamame",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_FROZEN,
    purchase = PURCHASE_MONTHLY,
    )

ING_PEANUT_BUTTER = IngredientKind(
    name = "Peanut butter",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_SESAME_SEEDS = IngredientKind(
    name = "Sesame seeds",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_SOY_SAUCE = IngredientKind(
    name = "Soy sauce",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_MISO = IngredientKind(
    name = "Miso",
    unit = UNIT_TBSPS,
    store = STORE_SPECIALTY,
    section = SECTION_SPECIALTY,
    purchase = PURCHASE_MONTHLY,
    )

ING_PREPARED_SOUP = IngredientKind(
    name = "Prepared soup",
    unit = UNIT_CUPS,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_HONEY = IngredientKind(
    name = "Honey",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_RICE_WINE_VINEGAR = IngredientKind(
    name = "Rice wine vinegar",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_ASIAN,
    purchase = PURCHASE_MONTHLY,
    )

ING_SESAME_OIL = IngredientKind(
    name = "Sesame oil",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_ASIAN,
    purchase = PURCHASE_MONTHLY,
    )

ING_SRIRACHA = IngredientKind(
    name = "Sriracha",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_ASIAN,
    purchase = PURCHASE_MONTHLY,
    )

ING_RED_BELL_PEPPERS = IngredientKind(
    name = "Red bell peppers",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_PORTABELLA_MUSHROOM_CAPS = IngredientKind(
    name = "Portabella mushroom caps",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_WATER_CHESTNUTS = IngredientKind(
    name = "Water chestnuts",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_ASIAN,
    purchase = PURCHASE_MONTHLY,
    )

ING_GREEN_ONIONS = IngredientKind(
    name = "Green onions",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_WALNUTS = IngredientKind(
    name = "Walnuts",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_BUTTER_LETTUCE = IngredientKind(
    name = "Butter lettuce",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_SUSHI_RICE = IngredientKind(
    name = "Sushi rice",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_CARROTS = IngredientKind(
    name = "Carrots",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_GINGER = IngredientKind(
    name = "Ginger",
    unit = UNIT_TBSPS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_APPLES = IngredientKind(
    name = "Apples",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_DIJON_MUSTARD = IngredientKind(
    name = "Dijon mustard",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_TOMATOES = IngredientKind(
    name = "Tomatoes",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_SILKEN_TOFU = IngredientKind(
    name = "Silken Tofu",
    unit = UNIT_PACKAGES,
    store = STORE_WINCO,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_MONTHLY,
    )

ING_BONITO_FLAKES = IngredientKind(
    name = "Bonito flakes",
    unit = UNIT_OZS,
    store = STORE_SPECIALTY,
    section = SECTION_SPECIALTY,
    purchase = PURCHASE_MONTHLY,
    )

ING_KOMBU = IngredientKind(
    name = "Kombu",
    unit = UNIT_OZS,
    store = STORE_SPECIALTY,
    section = SECTION_SPECIALTY,
    purchase = PURCHASE_MONTHLY,
    )

ING_WAKAME = IngredientKind(
    name = "Wakame",
    unit = UNIT_OZS,
    store = STORE_SPECIALTY,
    section = SECTION_SPECIALTY,
    purchase = PURCHASE_MONTHLY,
    )

ING_PUMPKIN_PUREE = IngredientKind(
    name = "Pumpkin puree",
    unit = UNIT_OZS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_SHALLOTS = IngredientKind(
    name = "Shallots",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_COCONUT_MILK = IngredientKind(
    name = "Coconut milk",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_ASIAN,
    purchase = PURCHASE_MONTHLY,
    )

ING_CINNAMON = IngredientKind(
    name = "Cinnamon",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_WEEKLY,
    )

ING_NUTMEG = IngredientKind(
    name = "Nutmeg",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_WEEKLY,
    )

ING_EGGS = IngredientKind(
    name = "Eggs",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_DAIRY,
    purchase = PURCHASE_WEEKLY,
    )

ING_BLEU_CHEESE = IngredientKind(
    name = "Bleu cheese",
    unit = UNIT_OZS,
    store = STORE_GROCERY,
    section = SECTION_DAIRY,
    purchase = PURCHASE_WEEKLY,
    )

ING_TILAPIA_FILLETS = IngredientKind(
    name = "Tilapia fillets",
    unit = UNIT_EMPTY,
    store = STORE_COSTCO,
    section = SECTION_FROZEN,
    purchase = PURCHASE_MONTHLY,
    )

ING_THYME = IngredientKind(
    name = "Thyme",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_BLACK_PEPPER = IngredientKind(
    name = "Black pepper",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_PARMESAN_CHEESE = IngredientKind(
    name = "Parmesean cheese",
    unit = UNIT_OZS,
    store = STORE_COSTCO,
    section = SECTION_DAIRY,
    purchase = PURCHASE_MONTHLY,
    )

ING_PARSLEY = IngredientKind(
    name = "Parsley",
    unit = UNIT_TBSPS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_SALMON_FILLETS = IngredientKind(
    name = "Salmon fillets",
    unit = UNIT_EMPTY,
    store = STORE_COSTCO,
    section = SECTION_FROZEN,
    purchase = PURCHASE_MONTHLY,
    )

ING_ASPARAGUS = IngredientKind(
    name = "Asparagus",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_ARUGULA = IngredientKind(
    name = "Arugula",
    unit = UNIT_CUPS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_CHERRY_TOMATOES = IngredientKind(
    name = "Cherry tomatoes",
    unit = UNIT_CUPS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_CAULIFLOWER = IngredientKind(
    name = "Cauliflower",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_SODIUM_CITRATE = IngredientKind(
    name = "Sodium citrate",
    unit = UNIT_OZS,
    store = STORE_SPECIALTY,
    section = SECTION_SPECIALTY,
    purchase = PURCHASE_MONTHLY,
    )

ING_CHEDDAR_CHEESE = IngredientKind(
    name = "Cheddar cheese",
    unit = UNIT_OZS,
    store = STORE_COSTCO,
    section = SECTION_DAIRY,
    purchase = PURCHASE_MONTHLY,
    )

ING_PESTO = IngredientKind(
    name = "Pesto",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_SEASONAL_VEGETABLES = IngredientKind(
    name = "Seasaonal vegetables",
    unit = UNIT_SERVINGS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_SICHUAN_PEPPERCORNS = IngredientKind(
    name = "Sichuan peppercorns",
    unit = UNIT_TSPS,
    store = STORE_SPECIALTY,
    section = SECTION_SPECIALTY,
    purchase = PURCHASE_MONTHLY,
    )

ING_VEGETABLE_OIL = IngredientKind(
    name = "Vegetable oil",
    unit = UNIT_TBSPS,
    store = STORE_COSTCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_DRIED_CHILIS = IngredientKind(
    name = "Dried chilis",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_MONTHLY,
    )

ING_GREEN_BEANS = IngredientKind(
    name = "Green beans",
    unit = UNIT_LBS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_WHOLE_WHEAT_FLOUR = IngredientKind(
    name = "Whole wheat flour",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BAKING,
    purchase = PURCHASE_MONTHLY,
    )

ING_QUINOA = IngredientKind(
    name = "Quinoa",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_MINT = IngredientKind(
    name = "Mint",
    unit = UNIT_TBSPS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_CUCUMBERS = IngredientKind(
    name = "Cucumbers",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_WHOLE_WHEAT_PITAS = IngredientKind(
    name = "Whole wheat pitas",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_CURRY_POWDER = IngredientKind(
    name = "Curry powder",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_BROWN_LENTILS = IngredientKind(
    name = "Brown lentils",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_TOFU = IngredientKind(
    name = "Tofu",
    unit = UNIT_PACKAGES,
    store = STORE_WINCO,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_MONTHLY,
    )

ING_PEANUTS = IngredientKind(
    name = "Peanuts",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_BROCCOLI = IngredientKind(
    name = "Broccoli",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_KALE = IngredientKind(
    name = "Kale",
    unit = UNIT_CUPS,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_SALAD_KIT = IngredientKind(
    name = "Salad kit",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_MUSTARD = IngredientKind(
    name = "Mustard",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_BAKING_POWDER = IngredientKind(
    name = "Baking powder",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BAKING,
    purchase = PURCHASE_MONTHLY,
    )

ING_CRUSHED_RED_PEPPER = IngredientKind(
    name = "Crushed red pepper",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_MOLASSES = IngredientKind(
    name = "Molasses",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_BAKING,
    purchase = PURCHASE_MONTHLY,
    )

ING_APPLE_CIDER_VINEGAR = IngredientKind(
    name = "Apple cider vinegar",
    unit = UNIT_TBSPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_MUSTARD_POWDER = IngredientKind(
    name = "Mustard powder",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_TOMATO_SAUCE = IngredientKind(
    name = "Tomato Sauce",
    unit = UNIT_CANS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_SOUR_CREAM = IngredientKind(
    name = "Sour cream",
    unit = UNIT_TBSPS,
    store = STORE_GROCERY,
    section = SECTION_DAIRY,
    purchase = PURCHASE_WEEKLY,
    )

ING_WHEAT_BERRIES = IngredientKind(
    name = "Wheat berries",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_PURPLE_CABBAGE = IngredientKind(
    name = "Purple cabbage",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_BRUSSEL_SPROUTS = IngredientKind(
    name = "Brussel sprouts",
    unit = UNIT_EMPTY,
    store = STORE_GROCERY,
    section = SECTION_GROCERY,
    purchase = PURCHASE_WEEKLY,
    )

ING_SEA_SALT = IngredientKind(
    name = "Sea Salt",
    unit = UNIT_TSPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_TAHINI = IngredientKind(
    name = "Tahini",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_GROCERY,
    purchase = PURCHASE_MONTHLY,
    )

ING_SPRING_MIX_SALAD = IngredientKind(
    name = "Spring mix salad",
    unit = UNIT_CUPS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

ING_DRIED_CHICKPEAS = IngredientKind(
    name = "Dried chickpeas",
    unit = UNIT_CUPS,
    store = STORE_WINCO,
    section = SECTION_BULK,
    purchase = PURCHASE_MONTHLY,
    )

ING_DILL = IngredientKind(
    name = "Dill",
    unit = UNIT_TBSPS,
    store = STORE_GROCERY,
    section = SECTION_PRODUCE,
    purchase = PURCHASE_WEEKLY,
    )

RECIPES = [
    # Risotto
    # Mushroom and charred corn tacos
    Recipe(
        name = "Peanut-Sesame Slaw with Soba Noodles",
        url = "http://cookieandkate.com/2014/peanut-sesame-slaw-with-soba-noodles/",
        tags = [
            TAG_MONDAY,
            ],
        ingredients = [
            ING_SOBA_NOODLES(2, UNIT_CUPS),
            ING_PURPLE_CABBAGE(1),
            ING_BRUSSEL_SPROUTS(12),
            ING_CARROTS(4),
            ING_GREEN_ONIONS(1),
            ING_PEANUT_BUTTER(8, UNIT_TBSPS),
            ING_RICE_WINE_VINEGAR(3, UNIT_TBSPS),
            ING_SESAME_OIL(3, UNIT_TBSPS),
            ING_SOY_SAUCE(3, UNIT_TBSPS),
            ING_HONEY(2, UNIT_TBSPS),
            ING_GINGER(1, UNIT_TBSPS),
            ING_GARLIC(2, UNIT_CLOVES),
            ING_PEANUTS(1, UNIT_CUPS),
            ING_CILANTRO(1),
            ING_LIMES(1),
            ],
        ),
    Recipe(
        name = "Arugula, Carrot and Chickpea Salad with Wheat Berries",
        url = "http://cookieandkate.com/2012/arugula-carrot-and-chickpea-salad-with-wheat-berries/",
        tags = [
            TAG_MONDAY,
            ],
        ingredients = [
            ING_WHEAT_BERRIES(1, UNIT_CUPS),
            ING_CHICKPEAS(2, UNIT_CANS),
            ING_CARROTS(4),
            ING_CHEESE_FETA(4, UNIT_OZS),
            ING_ARUGULA(6, UNIT_CUPS),
            ING_OLIVE_OIL(4, UNIT_TBSPS),
            ING_HONEY(0.67, UNIT_TBSPS),
            ING_GARLIC(2, UNIT_CLOVES),
            ING_CRUSHED_RED_PEPPER(0.25, UNIT_TSPS),
            ING_LEMONS(1),
            ING_BLACK_PEPPER(0.5, UNIT_TSPS),
            ],
        ),
    Recipe(
        name = "Quinoa Black Bean Burrito Bowl",
        url = "https://toriavey.com/toris-kitchen/2012/05/quinoa-black-bean-burrito-bowls/",
        tags = [
            TAG_SUNDAY,
            ],
        ingredients = [
            ING_QUINOA(2, UNIT_CUPS),
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_ONIONS(0.5),
            ING_GARLIC(2, UNIT_CLOVES),
            ING_BLACK_BEANS(2, UNIT_CANS),
            ING_CILANTRO(1),
            ING_LIMES(1),
            ING_GREEN_LEAF_LETTUCE(1),
            ING_CHEDDAR_CHEESE(2, UNIT_OZS),
            ING_SOUR_CREAM(2, UNIT_TBSPS),
            ING_SALSA(1, UNIT_CUPS),
            ING_AVOCADOS(1),
            ],
        ),
    Recipe(
        name = "Quinoa Bowl with Poached Egg and Avocado",
        tags = [
            TAG_SUNDAY,
            ],
        ingredients = [
            ING_QUINOA(2, UNIT_CUPS),
            ING_EGGS(6),
            ING_AVOCADOS(2),
            ING_GREEN_ONIONS(1),
            ],
        ),
    Recipe(
        name = "Sloppy Lentils",
        tags = [
            TAG_WEDNESDAY,
            ],
        ingredients = [
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_ONIONS(1),
            ING_BROWN_LENTILS(1, UNIT_CUPS),
            ING_VEGETABLE_STOCK(2, UNIT_CUPS),
            ING_TOMATO_SAUCE(1, UNIT_CANS),
            ING_MOLASSES(1, UNIT_TBSPS),
            ING_APPLE_CIDER_VINEGAR(1, UNIT_TBSPS),
            ING_SOY_SAUCE(1, UNIT_TBSPS),
            ING_TOMATO_PASTE(0.5, UNIT_CANS),
            ING_GARLIC_POWDER(1, UNIT_TSPS),
            ING_MUSTARD_POWDER(1, UNIT_TSPS),
            ING_BURGER_BUNS(4),
            ],
        ),
    Recipe(
        name = "Baked Falafel with Creamy Tahini Dressing and Salad",
        url = "http://cookieandkate.com/2012/baked-falafel/",
        tags = [
            TAG_MONDAY,
            ],
        ingredients = [
            ING_OLIVE_OIL(4, UNIT_TBSPS),
            ING_DRIED_CHICKPEAS(1, UNIT_CUPS),
            ING_RED_ONIONS(1),
            ING_PARSLEY(1),
            ING_CILANTRO(1),
            ING_GARLIC(3, UNIT_CLOVES),
            ING_CUMIN(0.25, UNIT_TSPS),
            ING_CINNAMON(0.1, UNIT_TBSPS),
            ING_BLACK_PEPPER(0.5, UNIT_TSPS),
            ING_SEA_SALT(1, UNIT_TSPS),
            ING_TAHINI(0.25, UNIT_CUPS),
            ING_LEMONS(1),
            ING_MISO(1, UNIT_TBSPS),
            ING_GARLIC(2, UNIT_CLOVES),
            ING_DILL(2, UNIT_TBSPS),
            ING_CAYENNE_PEPPER(0.1, UNIT_TSPS),
            ING_SPRING_MIX_SALAD(4, UNIT_CUPS),
            ING_CHERRY_TOMATOES(1),
            ING_CUCUMBERS(1),
            ING_CHEESE_FETA(4, UNIT_OZS),
            ING_WHOLE_WHEAT_PITAS(4),
            ],
        ),
    Recipe(
        name = "Salad Kit",
        tags = [
            TAG_SIDE,
            TAG_EASY,
            ],
        ingredients = [
            ING_SALAD_KIT(1),
            ],
        ),
    Recipe(
        name = "Peanutty Quinoa Bowls",
        url = "http://ohmyveggies.com/recipe-peanutty-quinoa-bowls-two-make-baked-tofu/",
        tags = [
            TAG_THURSDAY,
            ],
        ingredients = [
            ING_QUINOA(1, UNIT_CUPS),
            ING_OLIVE_OIL(1, UNIT_TBSPS),
            ING_RED_BELL_PEPPERS(1),
            ING_BROCCOLI(1),
            ING_PEANUT_BUTTER(6, UNIT_TBSPS),
            ING_LIMES(1),
            ING_SOY_SAUCE(0.33, UNIT_TBSPS),
            ING_GINGER(0.33, UNIT_TBSPS),
            ING_TOFU(1, UNIT_PACKAGES),
            ING_PEANUTS(0.5, UNIT_CUPS),
            ],
        ),
    Recipe(
        name = "Spiced Lentil Soup",
        url = "http://cookieandkate.com/2015/vegan-lentil-soup-recipe/",
        tags = [
            TAG_SOUPS,
            ],
        ingredients = [
            ING_OLIVE_OIL(4, UNIT_TBSPS),
            ING_ONIONS(1),
            ING_CARROTS(2),
            ING_GARLIC(4, UNIT_CLOVES),
            ING_CUMIN(2, UNIT_TSPS),
            ING_CURRY_POWDER(1, UNIT_TSPS),
            ING_THYME(0.1, UNIT_TBSPS),
            ING_DICED_TOMATOES(1, UNIT_CANS),
            ING_BROWN_LENTILS(1, UNIT_CUPS),
            ING_VEGETABLE_STOCK(4, UNIT_CUPS),
            ING_KALE(2, UNIT_CUPS),
            ING_LEMONS(1),
            ],
        ),
    Recipe(
        name = "Fried Chickpea and Arugula Pita Sandwiches",
        tags = [
            TAG_WEDNESDAY,
            ],
        ingredients = [
            ING_GREEK_YOGURT(16, UNIT_TBSPS),
            ING_MINT(3, UNIT_TBSPS),
            ING_LIMES(1),
            ING_GARLIC(2, UNIT_CLOVES),
            ING_CUCUMBERS(1),
            ING_WHOLE_WHEAT_PITAS(4),
            ING_CHICKPEAS(2, UNIT_CANS),
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_CUMIN(1, UNIT_TSPS),
            ING_SMOKED_PAPRIKA(1, UNIT_TSPS),
            ING_BLACK_PEPPER(1, UNIT_TSPS),
            ING_LEMONS(1),
            ING_ARUGULA(4, UNIT_CUPS),
            ING_TOMATOES(1),
            ],
        ),
    Recipe(
        name = "Quinoa",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_QUINOA(2, UNIT_CUPS),
            ],
        ),
    Recipe(
        name = "Whole Wheat Pizza",
        tags = [
            TAG_FRIDAY,
            TAG_SATURDAY,
            TAG_SUNDAY,
            TAG_FUN,
            TAG_GUESTS,
            ],
        ingredients = [
            ING_WHOLE_WHEAT_FLOUR(4, UNIT_CUPS),
            ING_CHEESE_MOZZARELLA(16, UNIT_OZS),
            ING_FRESH_BASIL(1),
            ING_DICED_TOMATOES(1, UNIT_CANS),
            ING_TOMATO_PASTE(1, UNIT_CANS),
            ING_BASIL(1, UNIT_TBSPS),
            ING_OREGANO(0.5, UNIT_TBSPS),
            ING_RED_WINE_VINEGAR(1, UNIT_TBSPS),
            ING_MUSHROOMS(1, UNIT_LBS),
            ING_YEAST(1, UNIT_TBSPS),
            ],
        ),
    Recipe(
        name = "Sichuan Dry-Fried Green Beans",
        url = "http://www.seriouseats.com/recipes/2015/03/20150305-sichuan-dry-fried-green-bean-broiled-food-lab-recipe.html",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_SICHUAN_PEPPERCORNS(1, UNIT_TSPS),
            ING_VEGETABLE_OIL(3, UNIT_TBSPS),
            ING_DRIED_CHILIS(1, UNIT_TBSPS),
            ING_GARLIC(4, UNIT_CLOVES),
            ING_GINGER(1, UNIT_TBSPS),
            ING_GREEN_ONIONS(1),
            ING_BLACK_PEPPER(1, UNIT_TSPS),
            ING_GREEN_BEANS(1, UNIT_LBS),
            ],
        ),
    Recipe(
        name = "Seasonal Vegetables",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_SEASONAL_VEGETABLES(4, UNIT_SERVINGS),
            ],
        ),
    Recipe(
        name = "Arugula and Pesto",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_ARUGULA(4, UNIT_CUPS),
            ING_PESTO(4, UNIT_TBSPS),
            ING_CHEESE_MOZZARELLA(2, UNIT_OZS),
            ],
        ),
    Recipe(
        name = "Riced Cauliflower and Cheese",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_CAULIFLOWER(0.5),
            ING_CHEDDAR_CHEESE(8, UNIT_OZS),
            ING_SODIUM_CITRATE(0.33, UNIT_OZS),
            ],
        ),
    Recipe(
        name = "Simple Italian Side Salad",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_SPINACH(3, UNIT_CUPS),
            ING_ARUGULA(3, UNIT_CUPS),
            ING_CHERRY_TOMATOES(1, UNIT_CUPS),
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_BASIL(1, UNIT_TBSPS),
            ING_RED_WINE_VINEGAR(1, UNIT_TBSPS),
            ING_PARMESAN_CHEESE(2, UNIT_OZS),
            ING_BLACK_PEPPER(1, UNIT_TSPS),
            ],
        ),
    Recipe(
        name = "Asparagus Roasted in Butter",
        tags = [
            TAG_SIDE,
            ],
        ingredients = [
            ING_ASPARAGUS(1),
            ING_BUTTER(2, UNIT_TBSPS),
            ING_GARLIC(1, UNIT_CLOVES),
            ],
        ),
    Recipe(
        name = "Salmon Roasted in Butter",
        url = "http://cooking.nytimes.com/recipes/5703-salmon-roasted-in-butter",
        tags = [
            TAG_FISH,
            TAG_TUESDAY,
            ],
        ingredients = [
            ING_SALMON_FILLETS(3),
            ING_BUTTER(4, UNIT_TBSPS),
            ING_PARSLEY(4, UNIT_TBSPS),
            ING_LEMONS(1),
            ],
        ),
    Recipe(
        name = "Lemon Garlic Tilapia",
        url = "http://allrecipes.com/recipe/89261/lemon-garlic-tilapia/",
        tags = [
            TAG_FISH,
            TAG_TUESDAY,
            ],
        ingredients = [
            ING_TILAPIA_FILLETS(4),
            ING_LEMONS(1),
            ING_BUTTER(1, UNIT_TBSPS),
            ING_GARLIC(2, UNIT_CLOVES),
            ING_PARSLEY(0.33, UNIT_TBSPS),
            ],
        ),
    Recipe(
        name = "Parmesean Crusted Tilapia FIllets",
        url = "http://allrecipes.com/recipe/228056/parmesan-crusted-tilapia-fillets/",
        tags = [
            TAG_FISH,
            TAG_TUESDAY,
            ],
        ingredients = [
            ING_TILAPIA_FILLETS(4),
            ING_PARMESAN_CHEESE(6, UNIT_OZS),
            ING_PARSLEY(1, UNIT_TBSPS),
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_PAPRIKA(2, UNIT_TSPS),
            ING_BLACK_PEPPER(1, UNIT_TSPS),
            ],
        ),        
    Recipe(
        name = "Cajun-Spiced Tilapia",
        url = "http://www.food.com/recipe/cajun-spiced-tilapia-487398",
        tags = [
            TAG_FISH,
            TAG_TUESDAY,
            ],
        ingredients = [
            ING_TILAPIA_FILLETS(4),
            ING_THYME(0.33, UNIT_TBSPS),
            ING_OREGANO(0.33, UNIT_TBSPS),
            ING_BLACK_PEPPER(0.33, UNIT_TSPS),
            ING_CAYENNE_PEPPER(0.25, UNIT_TSPS),
            ING_PAPRIKA(2, UNIT_TSPS),
            ING_GARLIC_POWDER(0.5, UNIT_TSPS),
            ING_BUTTER(3, UNIT_TBSPS),
            ],
        ),
    Recipe(
        name = "Simple Pumpkin Soup",
        url = "http://minimalistbaker.com/simple-pumpkin-soup/",
        tags = [
            TAG_SOUPS,
            ],
        ingredients = [
            ING_PUMPKIN_PUREE(29, UNIT_OZS),
            ING_SHALLOTS(2),
            ING_GARLIC(3, UNIT_CLOVES),
            ING_VEGETABLE_STOCK(4, UNIT_CUPS),
            ING_COCONUT_MILK(1, UNIT_CANS),
            ING_CINNAMON(0.25, UNIT_TBSPS),
            ING_NUTMEG(0.25, UNIT_TBSPS),
            ING_WALNUTS(0.5, UNIT_CUPS),
            ],
        ),
    Recipe(
        name = "Miso Soup",
        tags = [
            TAG_THURSDAY,
            ],
        ingredients = [
            ING_BONITO_FLAKES(2, UNIT_OZS),
            ING_KOMBU(1, UNIT_OZS),
            ING_WAKAME(1, UNIT_OZS),
            ING_MISO(4, UNIT_TBSPS),
            ING_EGGS(8),
            ING_SILKEN_TOFU(1, UNIT_PACKAGES),
            ING_GREEN_ONIONS(1),
            ],
        ),
    Recipe(
        name = "Bleu Cheese and Walnut Salad",
        tags = [
            TAG_MONDAY,
            ],
        ingredients = [
            ING_SPINACH(6, UNIT_CUPS),
            ING_BLEU_CHEESE(6, UNIT_OZS),
            ING_WALNUTS(1, UNIT_CUPS),
            ING_OLIVE_OIL(3, UNIT_TBSPS),
            ING_RED_WINE_VINEGAR(1, UNIT_TBSPS),
            ING_BASIL(1, UNIT_TBSPS),
            ING_APPLES(2),
            ING_DIJON_MUSTARD(1, UNIT_TBSPS),
            ],
        ),
    Recipe(
        name = "Asian Lettuce Wraps",
        url = "http://ohmyveggies.com/asian-lettuce-wraps/",
        tags = [
            TAG_THURSDAY,
            ],
        ingredients = [
            ING_SOY_SAUCE(4, UNIT_TBSPS),
            ING_PEANUT_BUTTER(2, UNIT_TBSPS),
            ING_MISO(1, UNIT_TBSPS),
            ING_HONEY(1, UNIT_TBSPS),
            ING_RICE_WINE_VINEGAR(0.67, UNIT_TBSPS),
            ING_GARLIC(1, UNIT_CLOVES),
            ING_SESAME_OIL(0.67, UNIT_TBSPS),
            ING_SRIRACHA(0.33, UNIT_TBSPS),
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_YELLOW_ONIONS(1),
            ING_RED_BELL_PEPPERS(1),
            ING_PORTABELLA_MUSHROOM_CAPS(1),
            ING_GINGER(0.67, UNIT_TBSPS),
            ING_WATER_CHESTNUTS(1, UNIT_CANS),
            ING_GREEN_ONIONS(1),
            ING_WALNUTS(0.33, UNIT_CUPS),
            ING_BUTTER_LETTUCE(1),
            ING_SUSHI_RICE(1, UNIT_CUPS),
            ING_CARROTS(3),
            ING_CILANTRO(0.5),
            ING_SESAME_SEEDS(2, UNIT_TBSPS),
            ],
        ),
    Recipe(
        name = "Eating Out",
        tags = [
            TAG_EASY,
            TAG_CIRCUMSTANCES,
            ],
        ingredients = [
            ],
        ),
    Recipe(
        name = "Eating Away from Home",
        tags = [
            TAG_CIRCUMSTANCES,
            ],
        ingredients = [
            ],
        ),
    Recipe(
        name = "Prepared Soup",
        tags = [
            TAG_EASY,
            ],
        ingredients = [
            ING_PREPARED_SOUP(8, UNIT_CUPS),
            ],
        ),
    Recipe(
        name = "Beck's Peanut Soba",
        tags = [
            TAG_THURSDAY,
            ],
        ingredients = [
            ING_SOBA_NOODLES(4, UNIT_CUPS),
            ING_FROZEN_EDAMAME(3, UNIT_CUPS),
            ING_PEANUT_BUTTER(6, UNIT_TBSPS),
            ING_SESAME_SEEDS(2, UNIT_TBSPS),
            ING_SOY_SAUCE(2, UNIT_TBSPS),
            ING_MISO(1, UNIT_TBSPS),
            ],
        ),
    Recipe(
        name = "Classic Paninis",
        tags = [
            TAG_WEDNESDAY,
            ],
        ingredients = [
            ING_BUTTER(2, UNIT_TBSPS),
            ING_SLICED_BREAD(8, UNIT_SLICES),
            ING_MAYONNAISE(2, UNIT_TBSPS),
            ING_RED_ONIONS(1),
            ING_BELL_PEPPERS(1),
            ING_MUSHROOMS(0.5, UNIT_LBS),
            ING_SPINACH(1, UNIT_CUPS),
            ING_CHEESE_MOZZARELLA(4, UNIT_OZS),
            ],
        ),
    Recipe(
        name = "Classic Bean Burritos",
        tags = [
            TAG_TUESDAY,
            ],
        ingredients = [
            ING_TORTILLAS(6),
            ING_BLACK_BEANS(1, UNIT_CANS),
            ING_ONIONS(1),
            ING_CHEESE_MOZZARELLA(6, UNIT_OZS),
            ING_PATO(1, UNIT_CANS),
            ],
        ),
    Recipe(
        name = "Vegetarian Taco Salad",
        url = "http://www.eatingwell.com/recipe/250064/vegetarian-taco-salad/",
        tags = [
            TAG_MONDAY,
            ],
        ingredients = [
            ING_OLIVE_OIL(2, UNIT_TBSPS),
            ING_ONIONS(1),
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
            ING_RED_WINE_VINEGAR(1, UNIT_TBSPS),
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
            ING_MAYONNAISE(3, UNIT_TBSPS),
            ING_GARLIC(3, UNIT_CLOVES),
            ING_LEMONS(1),
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
            ING_MAYONNAISE(3, UNIT_TBSPS),
            ING_BURGER_BUNS(4),
            ING_GREEN_LEAF_LETTUCE(1),
            ING_TOMATOES(1),
            ING_EGGS(4),
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
    Recipe(
        name = "New Recipe",
        tags = [
            TAG_FRIDAY,
            ],
        ingredients = [
            ],
        ),
    ]

RECIPES_INDEX = {r.name : r for r in RECIPES}
