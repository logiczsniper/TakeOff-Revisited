from pygame.sprite import Sprite
from pygame import Rect


class AnimatedSprite(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sheet, self.image = None, None
        self.frame = 0

    def update(self, current_states):

        self.clip(current_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

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
