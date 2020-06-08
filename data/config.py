# Probabilities
PROBAB_TIE = 10
PROBAB_SUICIDE = [0,  0,  1,  1,  1,  1,  1,  0]
PROBAB_REVIVE =  [0,  0,  1,  1,  1,  1,  1,  0]
PROBAB_TRAP =    [0,  1,  1,  1,  1,  1,  2,  2]
PROBAB_INFECT =  [0,  1,  1,  1,  1,  1,  2,  3]
PROBAB_DESTROY = [0,  0,  1,  1,  1,  1,  1,  2]
PROBAB_ATRACT =  [0,  1,  1,  1,  2,  5,  5,  5]
PROBAB_MONSTER = [0,  1,  2,  2,  3,  3,  3,  3]
PROBAB_STEAL =   [1,  1,  2,  6,  7,  7,  7,  7]
PROBAB_MOVE =    [7,  8,  9,  10,  12, 14, 15, 16]
PROBAB_ITEM =    [42, 38, 32, 29, 23, 18, 15, 15]
PROBAB_BATTLE = []

# Item rarities
PROBAB_RARITY_1 = 65
PROBAB_RARITY_2 = 30
PROBAB_RARITY_3 = 5
MAX_VALUE_RARITY_1 = 2
MAX_VALUE_RARITY_2 = 6

# Localization
LOCALIZATION = "es_wwe" #es_paramo, es_spain, es_interneto, es_wwe
if LOCALIZATION == "es_paramo":
    from data.es_paramo.config import *
elif LOCALIZATION == "es_spain":
    from data.es_spain.config import *
elif LOCALIZATION == "es_interneto":
    from data.es_interneto.config import *
elif LOCALIZATION == "es_wwe":
    from data.es_wwe.config import *

# If MATCH_TYPE = Match_type.districts
MAX_TRIBUTES_PER_DISTRICT = 3

# If MATCH_TYPE = Match_type.rumble
LIMIT_TIME_RUMBLE = 3

# Calculations
RANKING_IMG_SIZE = RANKING_AVATAR_SIZE + 2
RANKING_SPACE_BETWEEN_COLS = RANKING_PADDING
RANKING_FIRST_COLUMN_X = RANKING_PADDING
RANKING_FIRST_ROW_Y = RANKING_IMG_SIZE + RANKING_PADDING + RANKING_DISTRICT_NAME_HEIGHT
RANKING_WIDTH = RANKING_IMGS_PER_ROW * RANKING_IMG_SIZE + (RANKING_IMGS_PER_ROW - 1) * RANKING_SPACE_BETWEEN_COLS + RANKING_PADDING * 2
RANKING_DELTA_X = RANKING_IMG_SIZE + RANKING_SPACE_BETWEEN_COLS
RANKING_SPACE_BETWEEN_DISTRICTS = RANKING_PADDING / 2
RANKING_SPACE_BETWEEN_ROWS = RANKING_IMG_SIZE * 2 + RANKING_PADDING + int(RANKING_SPACE_BETWEEN_DISTRICTS/2) + RANKING_DISTRICT_NAME_HEIGHT

if len(PROBAB_BATTLE) > 0:
    sys.exit('Config error: PROBAB_BATTLE shouldnt be manually configured')
for i, probab in enumerate(PROBAB_SUICIDE):
    PROBAB_BATTLE.append(100 - (PROBAB_SUICIDE[i] + PROBAB_REVIVE[i] + PROBAB_TRAP[i] + PROBAB_INFECT[i] + PROBAB_DESTROY[i] + PROBAB_ATRACT[i] + PROBAB_MONSTER[i]+ PROBAB_STEAL[i] + PROBAB_MOVE[i] + PROBAB_ITEM[i]))
TREASONS_ENABLED_LIST =  [False, False, False, True, True, True, True, True]
