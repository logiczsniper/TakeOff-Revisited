from constants import Constants
from playerSprite import Rocket
from pygame.sprite import GroupSingle, Group
from pygame import display, time, event as py_event, QUIT, sprite, K_ESCAPE, sysfont
from scenes import *
from resources import Resources


class Game:
    def __init__(self):
        self.screen = display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        display.set_caption('TakeOff')
        self.resources = Resources()
        display.set_icon(self.resources.ICON)
        self.enemies = Group()
        self.rocket_group = GroupSingle()
        self.rocket = Rocket((20, 20), self.rocket_group)
        self.all_sprites = Group(self.rocket, self.enemies)
        self.active_scene = TitleScene()

        self.done = False
        self.clock = time.Clock()

    def run(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            display.flip()
            self.clock.tick(Constants.FPS)

    def event_loop(self):
        for event in py_event.get():
            if event.type == QUIT:
                self.done = True

            try:
                # Event is not always a key down, so event does not always have attribute 'key'

                # Give each event to the rocket's event handler which will also update it
                self.rocket.handle_event(event)

                if event.key == K_ESCAPE:
                    self.active_scene = PauseScene()
            except AttributeError:
                pass

    def update(self):

        # Spawn enemies
        # TODO

        # Update elevation
        font = sysfont.SysFont("arial", 30)
        text = font.render("Kilometres: " + str(self.rocket.elevation), True, Constants.BLACK)
        self.screen.blit(text, (1, 1))

        # Check if the user has surpassed their level via elevation
        # TODO map switching
        self.active_scene = self.active_scene.next

        # Check for collisions
        if sprite.spritecollide(self.rocket, self.enemies, False, sprite.collide_mask):
            self.active_scene = CrashScene()
        else:
            pass

    def draw(self):
        self.active_scene.render(self.screen)
        self.all_sprites.draw(self.screen)
