from pygame import time, event as py_event, sprite, MOUSEMOTION
from pygame.sprite import GroupSingle, Group

from playerSprite import Rocket
from scenes import *


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
                if event.type == KEYDOWN and event.key == K_ESCAPE and not isinstance(self.active_scene, PauseScene):
                    self.active_scene = PauseScene(self.active_scene)
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
            self.increment_level(SecondLevelScene())
        elif self.rocket.elevation == 2000:
            self.increment_level(ThirdLevelScene())
        elif self.rocket.elevation == 3000:
            self.active_scene = VictoryScene()

        # Update rocket
        self.rocket.handle_event()

        # Check for collisions
        if sprite.spritecollide(self.rocket, self.enemies, False, sprite.collide_mask):
            self.active_scene = CrashScene()
        else:
            pass

        self.active_scene = self.active_scene.next

    def increment_level(self, next_level_scene):
        self.active_scene = MidLevelScene()
        self.active_scene.render(self.screen)
        self.active_scene = next_level_scene

    def draw(self):
        self.active_scene.render(screen=self.screen)
        self.screen.blit(self.altitude_text, (3, 3))
        self.all_sprites.draw(self.screen)
