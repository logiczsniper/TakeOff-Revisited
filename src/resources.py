from constants import Constants
from pygame import image, mixer


class Resources:

    # Image Loader
    @staticmethod
    def load_image(folder, name):

        loaded_image = image.load(Constants.BASE_IMAGE_PATH.format(folder, name)).convert_alpha()
        return loaded_image

    # Sound loader
    @staticmethod
    def load_sound(folder, name):
        loaded_sound = mixer.Sound(Constants.BASE_SOUND_PATH.format(folder, name))
        return loaded_sound

    def __init__(self):
        # Images
        self.ICON = image.load(Constants.WINDOW_ICON).convert_alpha()
        self.ROCKET_SHEET = self.load_image("sprites", "rocket_sheet")

        self.TITLE_BG = self.load_image("backgrounds", "intro")
        self.VICTORY_BG = self.load_image("backgrounds", "victory")
        self.CRASH_BG = self.load_image("backgrounds", "crashed")
        self.PAUSE_BG = self.load_image("backgrounds", "paused")
        self.MIDLEVEL_BG = self.load_image("backgrounds", "mid_level")
        self.FIRST_BG = self.load_image("backgrounds", "level_one")
        self.SECOND_BG = self.load_image("backgrounds", "level_two")
        self.THIRD_BG = self.load_image("backgrounds", "level_three")

        # Sounds
        pass
