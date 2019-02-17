from resources import Resources
from pygame import event as pg_event, display, QUIT, quit as pg_quit, KEYDOWN, K_ESCAPE
from time import sleep
from constants import Constants
from sys import exit
from abc import abstractmethod, ABC


class SceneBase(ABC):
    def __init__(self):
        self.next = self
        self.resources = Resources()

    @abstractmethod
    def render(self, screen):
        pass

    @staticmethod
    def display_static_background(screen, background, text, text_x):
        screen.blit(background, (0, 0))
        screen.blit(Constants.FONT.render(text, True, Constants.BLACK),
                    (text_x, Constants.WINDOW_HEIGHT / 1.15))

    @staticmethod
    def check_quit(event):
        if event.type == QUIT:
            pg_quit()
            exit()

    def switch_to_scene(self, next_scene):
        self.next = next_scene
        return True

    def terminate(self):
        self.switch_to_scene(None)


class TitleScene(SceneBase):
    def __init__(self):
        super().__init__()

    def render(self, screen):
        self.display_static_background(screen, self.resources.TITLE_BG, "Press anywhere to play!",
                                       Constants.WINDOW_WIDTH / 2 - 180)
        while True:

            for event in pg_event.get():

                self.check_quit(event)

                if event.type == KEYDOWN:
                    self.switch_to_scene(LevelScene(self.resources.FIRST_BG, 0.5))
                    break
            else:
                display.update()
                continue

            break


class PauseScene(SceneBase):
    def __init__(self, current_level):
        super().__init__()
        self.current_level = current_level

    def render(self, screen):
        self.display_static_background(screen, self.resources.PAUSE_BG, "Press anywhere to resume!",
                                       Constants.WINDOW_WIDTH / 2 - 198)

        while True:

            for event in pg_event.get():

                self.check_quit(event)

                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.switch_to_scene(self.current_level)
                    break

            else:
                display.update()
                continue

            break


class MidLevelScene(SceneBase):
    def __init__(self):
        super().__init__()

    def render(self, screen):
        self.display_static_background(screen, self.resources.MIDLEVEL_BG, "Next Level",
                                       Constants.WINDOW_WIDTH / 2 - 70)
        display.update()
        sleep(4)


class EndScene(SceneBase):

    def __init__(self, background, text, text_x):
        super().__init__()
        self.background = background
        self.text = text
        self.text_x = text_x

    def render(self, screen):
        self.display_static_background(screen, self.background, self.text,
                                       self.text_x)

        while True:

            for event in pg_event.get():

                self.check_quit(event)

            else:
                display.update()
                continue


class LevelScene(SceneBase):

    def __init__(self, background, scroll_speed):
        super().__init__()
        self.background = background
        self.scroll_speed = scroll_speed
        self.y = 0

    def display_scrolling_background(self, screen, image, speed):
        rel_y = self.y % image.get_rect().height
        screen.blit(image, (0, rel_y - image.get_rect().height))
        if rel_y < Constants.WINDOW_HEIGHT:
            screen.blit(image, (0, rel_y))
        self.y += speed
        display.update()

    def render(self, screen):
        self.display_scrolling_background(screen, self.background, self.scroll_speed)
