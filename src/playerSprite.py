from animatedSprite import AnimatedSprite
from pygame import Rect
from constants import Constants
from resources import Resources


class Rocket(AnimatedSprite):
    def __init__(self, position, *groups):
        self.sheet = Resources().ROCKET_SHEET
        self.sheet.set_clip(Rect(0, 0, 56, 148))
        self.elevation = 0
        self.frames = {0: (0, 0, 56, 149), 1: (56, 0, 56, 164), 2: (112, 0, 56, 149), 3: (168, 0, 56, 132)}

        super().__init__(position, self.sheet, *groups)

    def handle_event(self):

        if self.rect.right > Constants.WINDOW_WIDTH:
            self.rect.right = Constants.WINDOW_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Constants.WINDOW_HEIGHT:
            self.rect.bottom = Constants.WINDOW_HEIGHT

        self.update(self.frames)
