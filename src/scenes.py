from abc import abstractmethod, ABC
from sys import exit
from time import sleep

from pygame import event as pg_event, display, QUIT, quit as pg_quit, MOUSEBUTTONDOWN

from constants import Constants
from resources import Resources


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

    def switch_to_scene(self, next_scene):
        self.next = next_scene
        return True


class StaticScene(SceneBase):
    def __init__(self, background, text, text_x, on_click=None, current_level=None):
        super().__init__()
        self.text_x = text_x
        self.text = text
        self.background = background
        self.on_click = on_click
        self.current_level = current_level

    def set_on_click(self, value):
        self.on_click = value

    def render(self, screen):
        self.display_static_background(screen, self.background, self.text, self.text_x)

        while True:

            for event in pg_event.get():

                if event.type == QUIT:
                    pg_quit()
                    exit()

                if event.type == MOUSEBUTTONDOWN:
                    self.on_click()
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
