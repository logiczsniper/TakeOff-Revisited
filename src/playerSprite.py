from animatedSprite import AnimatedSprite
from pygame import Rect
from constants import Constants
from resources import Resources


class Rocket(AnimatedSprite):
    def __init__(self, position, *groups):
        self.sheet = Resources().ROCKET_SHEET
        self.sheet.set_clip(Rect(0, 0, 55, 103))
        self.elevation = 0
        self.frames = Constants.ROCKET_FRAMES

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
