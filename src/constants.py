from pygame.font import Font
from pygame import init

# Initialize pygame.
init()


class Constants:
    # Title.
    TITLE = "TakeOff"

    # Text.
    FONT = Font("font/PressStart2P.ttf", 16)
    MESSAGE = "Click to {}!"

    # Colour.
    BLACK = (50, 50, 50)

    # Paths.
    BASE_IMAGE_PATH = "images/{}/{}.png"
    BASE_SOUND_PATH = "sounds/{}/{}.wav"

    # Window Characteristics.
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 800
    WINDOW_ICON = "images/icon.png"
    FPS = 25

    # Button Sizes.
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 80

    # Sprite Frames in the form -> {"direction": {frame_count: (topleft.x, topleft.y, width, height), ...}, ...}.
    ROCKET_FRAMES = {0: (0, 0, 55, 147), 1: (56, 0, 55, 163), 2: (112, 0, 55, 146), 3: (168, 0, 55, 131)}
    BIRD_FRAMES = {
        "right": {0: (0, 0, 63, 47), 1: (66, 0, 59, 41), 2: (0, 59, 60, 45), 3: (66, 0, 59, 41)},
        "left": {0: (187, 0, 63, 47), 1: (125, 6, 59, 41), 2: (190, 59, 60, 45), 3: (125, 6, 59, 41)}}
    HELICOPTER_FRAMES = {
        "right": {0: (0, 81, 155, 80), 1: (162, 81, 155, 80), 2: (326, 81, 155, 80), 3: (162, 81, 155, 80)},
        "left": {0: (326, 0, 155, 80), 1: (164, 0, 155, 80), 2: (0, 0, 155, 80), 3: (164, 0, 155, 80)}}
    SATELLITE_FRAMES = {
        "right": {0: (293, 0, 140, 122), 1: (445, 0, 140, 122)},
        "left": {0: (0, 0, 140, 122), 1: (152, 0, 140, 122)}}
