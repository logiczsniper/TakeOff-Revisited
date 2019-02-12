from animatedSprite import AnimatedSprite
from pygame import Rect, QUIT, quit as py_quit, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP, KEYUP


class Rocket(AnimatedSprite):
    def __init__(self, position, *groups):
        super().__init__(*groups)
        # TODO self.sheet =
        self.sheet.set_clip(Rect(55, 0, 47, 52))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.velocity = 5
        self.acceleration = 0.5

        # TODO frames
        self.left_states = {0: (1, 52, 45, 53), 1: (54, 52, 44, 53), 2: (106, 52, 45, 53)}
        self.right_states = {0: (7, 105, 44, 52), 1: (59, 105, 44, 52), 2: (112, 105, 44, 52)}
        self.up_states = {0: (8, 157, 43, 53), 1: (61, 157, 42, 53), 2: (113, 157, 43, 53)}
        self.down_states = {0: (3, 0, 44, 52), 1: (55, 0, 47, 52), 2: (108, 0, 46, 52)}

    def handle_event(self, event):

        if self.velocity > self.acceleration / 2:
            self.velocity -= self.acceleration / 2

        if event.type == QUIT:
            py_quit()
            quit()

        # TODO ensure user cannot leave screen here
        # TODO rotate rocket based on direction

        if event.type == KEYDOWN:
            self.velocity += self.acceleration

        elif event.type == KEYUP:
            self.velocity -= self.acceleration

        current_states = None

        if event.key == K_LEFT:
            self.rect.x -= self.velocity
            current_states = self.left_states
        if event.key == K_RIGHT:
            self.rect.x += self.velocity
            current_states = self.right_states
        if event.key == K_UP:
            self.rect.y -= self.velocity
            current_states = self.up_states
        if event.key == K_DOWN:
            self.rect.y += self.velocity
            current_states = self.down_states

        self.update(current_states)
