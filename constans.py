RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

MINE_FIELD_COLS = 50
MINE_FIELD_ROWS = 25

SQUARE_WIDTH = int(WINDOW_WIDTH / MINE_FIELD_COLS)
SQUARE_HEIGHT = int(WINDOW_HEIGHT / MINE_FIELD_ROWS)

# ====================================================================================================

SNAKE_IMG = "snake.png"

# ====================================================================================================

SOLDIER_IMG = "soldier.png"
SOLDIER_NIGHT_IMG = "soldier_night.png"
INJURY_IMG = "injury.png"
STEP = 1

SOLDIER_ROWS_MATRIX = 4
SOLDIER_COLS_MATRIX = 2
SOLDIER_ROWS_PIXL = 4
SOLDIER_COLS_PIXL = 4

SOLDIER_START_LOCATION_MATRIX = (0, 1)
SOLDIER_START_LOCATION_PIXL = (0, 0)

SOLDIER_SIZE = (SOLDIER_COLS_PIXL * SQUARE_WIDTH, SOLDIER_ROWS_PIXL * SQUARE_HEIGHT)

SOLDIER_START_MATRIX = \
    [[(0, 0), (0, 1)]
        , [(1, 0), (1, 1)]
        , [(2, 0), (2, 1)]
        , [(3, 0), (3, 1)]]

# ====================================================================================================

EXPLOTION_IMG = "explotion.png"
MINE_IMG = "mine.png"
MINE_SIZE = (SQUARE_WIDTH * 3, SQUARE_HEIGHT * 1)
MINES_NUMBER = 20
MINE_ROWS = 1
MINE_COLS = 3

# ====================================================================================================

FLAG_IMG = "flag.png"

FLAG_LOC_MATRIX_LIST = [(21, 46), (21, 47), (21, 48), (21, 49)
    , (22, 46), (22, 47), (22, 48), (22, 49)
    , (23, 46), (23, 47), (23, 48), (23, 49)]

FLAG_ROWS = 3
FLAG_COLS = 4
FlAG_SIZE = (FLAG_COLS * SQUARE_WIDTH, (FLAG_ROWS + 1) * SQUARE_HEIGHT)
FLAG_LOCATION_PIXL = (WINDOW_WIDTH - FlAG_SIZE[0], WINDOW_HEIGHT - FlAG_SIZE[1])

# ====================================================================================================

GRASS_IMG = "grass.png"
GRASS_SIZE = (50, 50)
GRASS_NUMBER = 20
# ====================================================================================================

BLACK = (0, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
BACKGROUND_COLOR = (76, 200, 56)

# ----------------------------------lose message-----------------------------------
FONT_NAME = "Calibri"
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))

# ----------------------------------win message-----------------------------------
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
