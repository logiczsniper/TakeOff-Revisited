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

        # Create loop scene that will function as the title screen
        self.active_scene = StaticScene(self.resources.TITLE_BG, "play", Constants.WINDOW_WIDTH / 2 - 180)

        # Must set the on click lambda after creation as it needs access to switch_to_scene
        self.active_scene.set_on_click(
            lambda: self.active_scene.switch_to_scene(LevelScene(self.resources.FIRST_BG, 0.5)))
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
            elif event.type == MOUSEBUTTONDOWN:

                # Create loop scene that will function as a pause screen, already have access to switch_to_scene
                self.active_scene = StaticScene(self.resources.PAUSE_BG, "resume", Constants.WINDOW_WIDTH / 2 - 180,
                                                lambda: self.active_scene.switch_to_scene(
                                                  self.active_scene.current_level), self.active_scene)

    def update(self):

        # Spawn enemies
        # TODO

        # Update elevation
        self.rocket.elevation += 1
        self.altitude_text = Constants.FONT.render("Altitude: " + str(self.rocket.elevation), True,
                                                   Constants.BLACK)

        # Check if the user has surpassed their level via elevation
        if self.rocket.elevation == 1000:
            self.increment_level(self.resources.SECOND_BG, 1)
        elif self.rocket.elevation == 2000:
            self.increment_level(self.resources.THIRD_BG, 1.5)
        elif self.rocket.elevation == 3000:

            # Create loop scene that will function as a victory screen, already have access to switch_to_scene
            self.active_scene = StaticScene(self.resources.VICTORY_BG, "quit", Constants.WINDOW_WIDTH / 2 - 170,
                                            lambda: quit())

        # Update rocket
        self.rocket.handle_event()

        # Check for collisions
        if sprite.spritecollide(self.rocket, self.enemies, False, sprite.collide_mask):

            # Create loop scene that will function as a loss screen, already have access to switch_to_scene
            self.active_scene = StaticScene(self.resources.CRASH_BG, "quit", Constants.WINDOW_WIDTH / 2 - 170,
                                            lambda: quit())
        else:
            pass

        self.active_scene = self.active_scene.next

    def increment_level(self, next_background, next_scroll_speed):
        self.active_scene = MidLevelScene()
        self.active_scene.render(self.screen)
        self.active_scene = LevelScene(next_background, next_scroll_speed)

    def draw(self):
        self.active_scene.render(screen=self.screen)
        self.screen.blit(self.altitude_text, (3, 3))
        self.all_sprites.draw(self.screen)
