# Probabilities
PROBAB_TIE = 10
PROBAB_SUICIDE = [0,  0,  1,  0,  1,  0,  1,  0]
PROBAB_REVIVE =  [0,  0,  1,  1,  1,  1,  0,  0]
PROBAB_TRAP =    [0,  1,  1,  1,  1,  1,  2,  2]
PROBAB_INFECT =  [0,  1,  1,  1,  1,  1,  1,  1]
PROBAB_DESTROY = [0,  0,  1,  1,  1,  1,  1,  2]
PROBAB_INJURE =  [0,  0,  1,  1,  1,  1,  1,  1]
PROBAB_ATRACT =  [0,  1,  1,  1,  2,  5,  5,  5]
PROBAB_MONSTER = [0,  1,  2,  2,  3,  3,  3,  3]
PROBAB_STEAL =   [1,  1,  2,  6,  7,  7,  7,  7]
PROBAB_MOVE =    [7,  8,  8,  9,  11, 14, 15, 16]
PROBAB_ITEM =    [42, 38, 32, 30, 23, 18, 16, 16]
PROBAB_BATTLE =  [50, 49, 49, 47, 48, 48, 48, 47]
TREASONS_ENABLED_LIST =  [False, False, False, True, True, True, True, True]

# Item rarities
PROBAB_RARITY_1 = 65
PROBAB_RARITY_2 = 30
PROBAB_RARITY_3 = 5
MAX_VALUE_RARITY_1 = 2
MAX_VALUE_RARITY_2 = 6

# Localization
LOCALIZATION = "es_interneto" #es_paramo, es_spain, es_interneto
if LOCALIZATION == "es_paramo":
    from data.es_paramo.config import *
elif LOCALIZATION == "es_spain":
    from data.es_spain.config import *
elif LOCALIZATION == "es_interneto":
    from data.es_interneto.config import *
