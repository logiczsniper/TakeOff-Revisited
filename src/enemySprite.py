from animatedSprite import AnimatedSprite
from pygame import Rect
from constants import Constants


class Enemy(AnimatedSprite):
    def __init__(self, sheet, direction, position, speed, frames, y_change, *groups):
        self.sheet = sheet
        self.sheet.set_clip(Rect(frames.get(1)))
        self.elevation = 0
        self.y_change = y_change
        self.direction = direction

        # Adds direction via determining if speed should be negative, hence velocity
        self.velocity = speed if self.direction == "right" else -speed
        self.frames = frames

        super().__init__(position, self.sheet, *groups)

    def handle_event(self):
        if self.direction == "right" and self.rect.left > Constants.WINDOW_WIDTH or \
                self.direction == "left" and self.rect.right < 0:
            self.kill()
        else:
            self.rect.x += self.velocity
            self.rect.y += self.y_change

        self.update(self.frames)
