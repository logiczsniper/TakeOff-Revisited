from pygame import time, event as py_event, sprite, MOUSEMOTION, mixer
from pygame.sprite import GroupSingle, Group

from random import choice, randint

from playerSprite import Rocket
from enemySprite import Enemy
from scenes import *


class Game:
    """
    The entire game is contained in this class or implemented in this class, i.e, all of the scene
    classes are implemented here.
    """

    def __init__(self):

        # Set up display, gain access to all the resources, make these resources accessible throughout the class.
        self.screen = display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        display.set_caption('TakeOff')
        self.resources = Resources()
        display.set_icon(self.resources.ICON)

        # Set up groups.
        self.enemies = Group()
        self.rocket_group = GroupSingle()

        # Create the player (rocket).
        self.rocket = Rocket((20, 20), self.rocket_group)

        self.all_sprites = Group(self.rocket, self.enemies)

        # Create a generator so I can use the next() to get the next enemy that will be displayed.
        self.current_enemy_generator = self.generate_sprite_sheet()
        self.current_enemy = next(self.current_enemy_generator)

        # Create loop scene that will function as the title screen.
        self.active_scene = StaticScene(self.resources.TITLE_BG, Constants.MESSAGE.format("play"),
                                        Constants.WINDOW_WIDTH / 2 - 110)

        # Must set the on click lambda after creation as it needs access to switch_to_scene.
        self.active_scene.set_on_click(
            lambda: self.active_scene.switch_to_scene(LevelScene(self.resources.FIRST_BG, 2)))

        # Set initial values for the altitude text and the number of enemies.
        self.altitude_text = ""
        self.num_of_enemies = 2

        # Init mixer, start playing background music.
        mixer.init()
        mixer.music.load(Constants.BASE_SOUND_PATH.format("background", "background"))
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)

        # Set up loop, clock.
        self.done = False
        self.clock = time.Clock()

    def run(self):
        """
        Runs the game in a while loop.
        First, the newest pygame events are handled and passed to each sprite. Next, each sprite is updated and core
        game logic is applied. Next, all of the sprites and background are drawn before the display is updated, and the
        clock tick continues.
        """

        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            display.flip()
            self.clock.tick(Constants.FPS)

    def event_loop(self):
        """
        Handle all the events from pygame, the main event being mouse motion (as the rocket must follow this) and mouse
        click, which this function depends on the scene.
        """

        for event in py_event.get():
            if event.type == QUIT:
                self.done = True
            elif event.type == MOUSEMOTION:
                self.rocket.rect.center = event.pos
            elif event.type == MOUSEBUTTONDOWN:

                # Create loop scene that will function as a pause screen, already have access to switch_to_scene.
                self.active_scene = StaticScene(self.resources.PAUSE_BG, Constants.MESSAGE.format("resume"),
                                                Constants.WINDOW_WIDTH / 2 - 120,
                                                lambda: self.active_scene.switch_to_scene(
                                                    self.active_scene.current_level), self.active_scene)

    def update(self):
        """
        Apply core game logic including spawning enemies, detecting collisions and incrementing level.
        """

        # Spawn enemies.
        if len(self.enemies) < self.num_of_enemies and isinstance(self.active_scene,
                                                                  LevelScene) and self.rocket.elevation > 150:

            # Starting random direction (facing).
            direction = choice(["left", "right"])
            pos_y = randint(-80, Constants.WINDOW_HEIGHT - 360)

            if self.current_enemy == self.resources.BIRD_SHEET:

                sound_effect = self.resources.BIRD_SOUND
                Enemy(self.current_enemy, direction,
                      (Constants.WINDOW_WIDTH + 100 if direction == "left" else -100, pos_y), 2.2,
                      Constants.BIRD_FRAMES.get(direction), 2, self.enemies, self.all_sprites)

            elif self.current_enemy == self.resources.HELICOPTER_SHEET:

                sound_effect = self.resources.HELICOPTER_SOUND
                Enemy(self.current_enemy, direction,
                      (Constants.WINDOW_WIDTH + 160 if direction == "left" else -160, pos_y), 3.1,
                      Constants.HELICOPTER_FRAMES.get(direction), 3, self.enemies, self.all_sprites)

            elif self.current_enemy == self.resources.SATELLITE_SHEET:

                sound_effect = self.resources.SATELLITE_SOUND
                Enemy(self.current_enemy, direction,
                      (Constants.WINDOW_WIDTH + 145 if direction == "left" else -145, pos_y), 4,
                      Constants.SATELLITE_FRAMES.get(direction), 4, self.enemies, self.all_sprites)

            else:
                raise Exception("game.current_enemy incorrectly set")

            sound_effect.play()

        # Update elevation.
        self.rocket.elevation += 1
        self.altitude_text = Constants.FONT.render("Altitude: " + str(self.rocket.elevation), True,
                                                   Constants.BLACK)

        # Check if the user has surpassed their level via elevation.
        if self.rocket.elevation == 1000:
            self.increment_level(self.resources.SECOND_BG, 3)
        elif self.rocket.elevation == 2000:
            self.increment_level(self.resources.THIRD_BG, 4)
        elif self.rocket.elevation == 2500:

            # Increment number of enemies for the final 500 km.
            self.num_of_enemies += 1
        elif self.rocket.elevation == 3000:

            # Play victory sound.
            self.resources.VICTORY_SOUND.play()

            # Create loop scene that will function as a victory screen, already have access to switch_to_scene.
            self.active_scene = StaticScene(self.resources.VICTORY_BG, Constants.MESSAGE.format("quit"),
                                            Constants.WINDOW_WIDTH / 2 - 110, lambda: quit())

        # Update all sprites.
        for active_sprite in self.all_sprites:
            active_sprite.handle_event()

            if isinstance(active_sprite, Rocket):
                # Play rocket sound every update.
                self.resources.ROCKET_SOUND.play()

        # Check for collisions.
        if sprite.spritecollide(self.rocket, self.enemies, False, sprite.collide_mask):
            # Play crash sound.
            self.resources.CRASH_SOUND.play()

            # Create loop scene that will function as a loss screen, already have access to switch_to_scene.
            self.active_scene = StaticScene(self.resources.CRASH_BG, Constants.MESSAGE.format("quit"),
                                            Constants.WINDOW_WIDTH / 2 - 110, lambda: quit())

        # Update the active scene if changed.
        self.active_scene = self.active_scene.next

    def increment_level(self, next_background, next_scroll_speed):
        """
        Increase the level by one, which includes switching to the MidLevelScene. Resets game by clearing enemies,
        increments difficulty by increasing num_of_enemies, and gets the next() enemy.

        :param next_background: the resource for the background image of the next scene.
        :type: Surface

        :param next_scroll_speed: the speed of the scrolling background for the next scene.
        :type: int
        """

        self.active_scene = MidLevelScene()
        self.active_scene.render(self.screen)
        self.active_scene = LevelScene(next_background, next_scroll_speed)
        self.kill_enemies()
        self.num_of_enemies += 1
        self.current_enemy = next(self.current_enemy_generator)

    def kill_enemies(self):
        """
        Kills all enemy sprites.
        """

        for enemy in self.enemies:
            enemy.kill()

    def generate_sprite_sheet(self):
        """
        Generate the next enemy sprite sheet on request (will be requested each time the level is incremented).
        """

        for sheet in [self.resources.BIRD_SHEET, self.resources.HELICOPTER_SHEET, self.resources.SATELLITE_SHEET]:
            yield sheet

    def draw(self):
        """
        Render the active scene, display the altitude, draw all sprites.
        """

        self.active_scene.render(screen=self.screen)
        self.screen.blit(self.altitude_text, (3, 3))
        self.all_sprites.draw(self.screen)
