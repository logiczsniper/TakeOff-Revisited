from pygame.sprite import Sprite
from pygame.mask import from_surface
from pygame import Rect

from abc import abstractmethod, ABC


class AnimatedSprite(Sprite, ABC):
    """
    Every sprite that is animated has the variables and methods here in order to animate. Each sprite that inherits must
    however make its own handle_event(self) that determines it's logic in how it behaves and then calls update method.
    """

    def __init__(self, position, sheet, *groups):
        """
        Set variables needed for animation and set the mask which is needed for pixel perfect collision detection.

        :param position: the starting position of the sprite.
        :type: tuple

        :param sheet: the sprite sheet image that has been loaded.
        :type: Surface

        :param groups: which groups this new sprite belongs to.
        :type: Group or GroupSingle
        """
        super().__init__(*groups)
        self.sheet = sheet
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.mask = from_surface(self.image)

    def update(self, current_states):
        """
        Set the image of the sprite to the next image in the animation.

        :param current_states: the data structure found in Constants that contains information on how to clip each frame
        in the animation sequence.
        :type: dict
        """

        self.clip(current_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.mask = from_surface(self.image)

    def get_frame(self, frame_set):
        """
        Gets the next frame in the animation sequence.

        :param frame_set: the animation frame position and dimension information.
        :type: dict

        :return: the next frame in the animation sequence.
        :rtype: dict
        """

        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        """
        Set the clip from the sprite sheet image.

        :param clipped_rect: the animation frame position and dimension information for the specific frame.
        :type: dict

        :return: the clip of the main sprite sheet with the dimension and topleft position given by the clipped rect.
        :rtype: RectType
        """

        if type(clipped_rect) is dict:
            self.sheet.set_clip(Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(Rect(clipped_rect))
        return clipped_rect

    @abstractmethod
    def handle_event(self):
        """
        Method must be overwritten by each child class as it must contain the logic specific to the actions of that
        specific child and then call update().
        """

        pass
