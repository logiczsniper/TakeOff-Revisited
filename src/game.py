from pygame import time, event as py_event, sprite, MOUSEMOTION
from pygame.sprite import GroupSingle, Group

from random import choice, randint

from playerSprite import Rocket
from enemySprite import Enemy
from scenes import *


class Game:
    def __init__(self):
        self.num_of_enemies = 2
        self.screen = display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        display.set_caption('TakeOff')
        self.resources = Resources()
        display.set_icon(self.resources.ICON)
        self.enemies = Group()
        self.rocket_group = GroupSingle()
        self.rocket = Rocket((20, 20), self.rocket_group)
        self.all_sprites = Group(self.rocket, self.enemies)
        self.current_enemy_generator = self.generate_sprite_sheet()
        self.current_enemy = next(self.current_enemy_generator)

        # Create loop scene that will function as the title screen
        self.active_scene = StaticScene(self.resources.TITLE_BG, Constants.MESSAGE.format("play"),
                                        Constants.WINDOW_WIDTH / 2 - 110)

        # Must set the on click lambda after creation as it needs access to switch_to_scene
        self.active_scene.set_on_click(
            lambda: self.active_scene.switch_to_scene(LevelScene(self.resources.FIRST_BG, 2)))
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
                self.active_scene = StaticScene(self.resources.PAUSE_BG, Constants.MESSAGE.format("resume"),
                                                Constants.WINDOW_WIDTH / 2 - 120,
                                                lambda: self.active_scene.switch_to_scene(
                                                    self.active_scene.current_level), self.active_scene)

    def update(self):

        # Spawn enemies
        if len(self.enemies) < self.num_of_enemies and isinstance(self.active_scene,
                                                                  LevelScene) and self.rocket.elevation > 150:

            # Starting random direction (facing)
            direction = choice(["left", "right"])

            if self.current_enemy == self.resources.BIRD_SHEET:
                frames = Constants.BIRD_FRAMES.get(direction)
                speed = 2.2
                pos_x = Constants.WINDOW_WIDTH + 100 if direction == "left" else -100
                y_change = 2
            elif self.current_enemy == self.resources.HELICOPTER_SHEET:
                frames = Constants.HELICOPTER_FRAMES.get(direction)
                speed = 3.1
                pos_x = Constants.WINDOW_WIDTH + 160 if direction == "left" else -160
                y_change = 3
            elif self.current_enemy == self.resources.SATELLITE_SHEET:
                frames = Constants.SATELLITE_FRAMES.get(direction)
                speed = 4
                pos_x = Constants.WINDOW_WIDTH + 145 if direction == "left" else -145
                y_change = 4
            else:
                raise Exception("game.current_enemy incorrectly set")

            pos_y = randint(-50, Constants.WINDOW_HEIGHT - 350)

            Enemy(self.current_enemy, direction, (pos_x, pos_y), speed, frames, y_change, self.enemies,
                  self.all_sprites)

        # Update elevation
        self.rocket.elevation += 1
        self.altitude_text = Constants.FONT.render("Altitude: " + str(self.rocket.elevation), True,
                                                   Constants.BLACK)

        # Check if the user has surpassed their level via elevation
        if self.rocket.elevation == 1000:
            self.increment_level(self.resources.SECOND_BG, 3)
        elif self.rocket.elevation == 2000:
            self.increment_level(self.resources.THIRD_BG, 4)
        elif self.rocket.elevation == 3000:

            # Create loop scene that will function as a victory screen, already have access to switch_to_scene
            self.active_scene = StaticScene(self.resources.VICTORY_BG, Constants.MESSAGE.format("quit"),
                                            Constants.WINDOW_WIDTH / 2 - 110, lambda: quit())

        # Update all sprites
        for active_sprite in self.all_sprites:
            active_sprite.handle_event()

        # Check for collisions
        if sprite.spritecollide(self.rocket, self.enemies, False, sprite.collide_mask):
            # Create loop scene that will function as a loss screen, already have access to switch_to_scene
            self.active_scene = StaticScene(self.resources.CRASH_BG, Constants.MESSAGE.format("quit"),
                                            Constants.WINDOW_WIDTH / 2 - 110, lambda: quit())

        self.active_scene = self.active_scene.next

    def increment_level(self, next_background, next_scroll_speed):
        self.active_scene = MidLevelScene()
        self.active_scene.render(self.screen)
        self.active_scene = LevelScene(next_background, next_scroll_speed)
        self.kill_enemies()
        self.num_of_enemies += 1
        self.current_enemy = next(self.current_enemy_generator)

    def kill_enemies(self):
        for enemy in self.enemies:
            enemy.kill()

    def generate_sprite_sheet(self):

        for sheet in [self.resources.BIRD_SHEET, self.resources.HELICOPTER_SHEET, self.resources.SATELLITE_SHEET]:
            yield sheet

    def draw(self):
        self.active_scene.render(screen=self.screen)
        self.screen.blit(self.altitude_text, (3, 3))
        self.all_sprites.draw(self.screen)
