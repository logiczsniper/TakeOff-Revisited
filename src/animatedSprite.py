from pygame.sprite import Sprite
from pygame.mask import from_surface
from pygame import Rect


class AnimatedSprite(Sprite):
    def __init__(self, position, sheet, *groups):
        super().__init__(*groups)
        self.sheet = sheet
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.mask = None

    def update(self, current_states):

        self.clip(current_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.mask = from_surface(self.image)

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(Rect(clipped_rect))
        return clipped_rect
