from animatedSprite import AnimatedSprite
from pygame import Rect
from constants import Constants


class Enemy(AnimatedSprite):
    """
    The base class used by all enemies.
    """

    def __init__(self, sheet, direction, position, speed, frames, y_change, *groups):
        """
        As it is used by all enemies, the following parameters are what determine which enemy this class becomes. This
        sets all of the required variables.

        :param sheet: the sprite sheet resource image.
        :type: Surface

        :param direction: the direction that the sprite is facing. Either "right" or "left".
        :type: str

        :param position: the starting position of the sprite.
        :type: tuple

        :param speed: the speed at which the sprite will travel vertically.
        :type: int

        :param frames: the data structure found in Constants that contains information on each Rect for each frame of
        the animation sequence.
        :type: dict

        :param y_change: the horizontal change in position.
        :type: int

        :param groups: the groups that the sprite belongs to.
        :type: Group or GroupSingle
        """

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
        """
        On each update, applies the logic that kills the sprite if it reaches the end of its path or updates the sprites
        position on the screen, then calls the animated sprite update().
        """

        if self.direction == "right" and self.rect.left > Constants.WINDOW_WIDTH or \
                self.direction == "left" and self.rect.right < 0:
            self.kill()
        else:
            self.rect.x += self.velocity
            self.rect.y += self.y_change

        self.update(self.frames)
