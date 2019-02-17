from pygame.font import Font
from pygame import init


init()


class Constants:
    # Title
    TITLE = "TakeOff"

    # Text
    FONT = Font("font/PressStart2P.ttf", 16)
    MESSAGE = "Click to {}!"

    # Colours
    GREEN = (113, 148, 41)
    DARK_GREEN = (34, 139, 34)

    RED = (165, 42, 42)
    DARK_RED = (180, 36, 36)

    BLUE = (25, 25, 112)
    DARK_BLUE = (5, 5, 132)

    PURPLE = (106, 90, 205)
    DARK_PURPLE = (132, 112, 255)

    BLACK = (50, 50, 50)
    WHITE = (255, 255, 255)

    # Paths
    BASE_IMAGE_PATH = "images/{}/{}.png"
    BASE_SOUND_PATH = "sounds/{}/{}.ogg"

    # Window Characteristics
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 800
    WINDOW_ICON = "images/icon.png"
    FPS = 25

    # Button Sizes
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 80
