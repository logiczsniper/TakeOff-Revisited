from animatedSprite import AnimatedSprite
from pygame import Rect
from constants import Constants


class Enemy(AnimatedSprite):
    def __init__(self, sheet, position, *groups):
        self.sheet = sheet
        # TODO: initial rect
        self.sheet.set_clip(Rect())
        self.elevation = 0
        self.left_frames = {0: (0, 0, 56, 149), 1: (56, 0, 56, 164), 2: (112, 0, 56, 149), 3: (168, 0, 56, 132)}
        self.right_frames = {0: (0, 0, 56, 149), 1: (56, 0, 56, 164), 2: (112, 0, 56, 149), 3: (168, 0, 56, 132)}

        super().__init__(position, self.sheet, *groups)

    def handle_event(self):

        # TODO: enemy logic to have them continue in their starting direction

        # TODO: logic to determine which frames to use (based on direction)
        self.update(self.frames)
