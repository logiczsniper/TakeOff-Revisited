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
    def load_sound(folder, name, volume):
        loaded_sound = mixer.Sound(Constants.BASE_SOUND_PATH.format(folder, name))
        loaded_sound.set_volume(volume)
        return loaded_sound

    def __init__(self):
        # Images
        self.ICON = image.load(Constants.WINDOW_ICON).convert_alpha()
        self.ROCKET_SHEET = self.load_image("sprites", "rocket")
        self.BIRD_SHEET = self.load_image("sprites", "bird")
        self.HELICOPTER_SHEET = self.load_image("sprites", "helicopter")
        self.SATELLITE_SHEET = self.load_image("sprites", "satellite")

        self.TITLE_BG = self.load_image("backgrounds", "intro")
        self.VICTORY_BG = self.load_image("backgrounds", "victory")
        self.CRASH_BG = self.load_image("backgrounds", "crashed")
        self.PAUSE_BG = self.load_image("backgrounds", "paused")
        self.MIDLEVEL_BG = self.load_image("backgrounds", "mid_level")
        self.FIRST_BG = self.load_image("backgrounds", "level_one")
        self.SECOND_BG = self.load_image("backgrounds", "level_two")
        self.THIRD_BG = self.load_image("backgrounds", "level_three")

        # Sounds
        self.ROCKET_SOUND = self.load_sound("effects", "rocket", 0.15)
        self.BIRD_SOUND = self.load_sound("effects", "bird", 0.6)
        self.HELICOPTER_SOUND = self.load_sound("effects", "helicopter", 0.6)
        self.SATELLITE_SOUND = self.load_sound("effects", "satellite", 0.6)
        self.CRASH_SOUND = self.load_sound("effects", "crash", 0.8)
        self.VICTORY_SOUND = self.load_sound("effects", "victory", 0.8)
