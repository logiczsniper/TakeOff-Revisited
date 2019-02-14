from constants import Constants
from playerSprite import Rocket
from pygame.sprite import GroupSingle, Group
from pygame import time, event as py_event, sprite, K_ESCAPE, sysfont, MOUSEMOTION
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
        self.altitude_text = ""

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
            elif event.type == MOUSEMOTION:
                self.rocket.rect.center = event.pos

            try:
                # Event is not always a key down, so event does not always have attribute 'key'
                if event.key == K_ESCAPE:
                    self.active_scene = PauseScene()
            except AttributeError:
                pass

    def update(self):

        # Spawn enemies
        # TODO

        # Update elevation
        self.rocket.elevation += 1
        self.altitude_text = Constants.FONT.render("Altitude: " + str(self.rocket.elevation), True,
                                                   Constants.BLACK)

        # Check if the user has surpassed their level via elevation
        if self.rocket.elevation == 1000:
            self.active_scene = MidLevelScene()
            self.active_scene.render(self.screen)
            self.active_scene = SecondLevelScene()
        elif self.rocket.elevation == 2000:
            self.active_scene = MidLevelScene()
            self.active_scene.render(self.screen)
            self.active_scene = ThirdLevelScene()
        elif self.rocket.elevation == 3000:
            self.active_scene = VictoryScene()

        self.active_scene = self.active_scene.next

        # Update rocket
        self.rocket.handle_event()

        # Check for collisions
        if sprite.spritecollide(self.rocket, self.enemies, False, sprite.collide_mask):
            self.active_scene = CrashScene()
        else:
            pass

    def draw(self):
        self.active_scene.render(self.screen)
        self.screen.blit(self.altitude_text, (1, 1))
        self.all_sprites.draw(self.screen)
