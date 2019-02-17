from resources import Resources
from pygame import event as pg_event, display, QUIT, quit as pg_quit, KEYDOWN, K_ESCAPE
from time import sleep
from constants import Constants
from sys import exit
from abc import abstractmethod, ABC


class SceneBase(ABC):
    def __init__(self):
        self.next = self
        self.y = 0
        self.resources = Resources()
        # TODO fix!

    @abstractmethod
    def render(self, screen):
        pass

    def display_scrolling_background(self, screen, image, speed):
        rel_y = self.y % image.get_rect().height
        screen.blit(image, (0, rel_y - image.get_rect().height))
        if rel_y < Constants.WINDOW_HEIGHT:
            screen.blit(image, (0, rel_y))
        self.y += speed
        display.update()

    def switch_to_scene(self, next_scene):
        self.next = next_scene
        return True

    def terminate(self):
        self.switch_to_scene(None)


class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.TITLE_BG, (0, 0))
        screen.blit(Constants.FONT.render("Press anywhere to play!", True, Constants.BLACK),
                    (Constants.WINDOW_WIDTH / 2 - 180, Constants.WINDOW_HEIGHT / 1.15))

        while True:

            for event in pg_event.get():

                if event.type == QUIT:
                    pg_quit()
                    exit()

                if event.type == KEYDOWN:
                    self.switch_to_scene(FirstLevelScene())
                    break
            else:
                display.update()
                continue

            break


class VictoryScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.VICTORY_BG, (0, 0))
        screen.blit(Constants.FONT.render("Press anywhere to quit!", True, Constants.BLACK),
                    (Constants.WINDOW_WIDTH / 2 - 180, Constants.WINDOW_HEIGHT / 1.15))

        while True:

            for event in pg_event.get():

                if event.type == QUIT or event.type == KEYDOWN:
                    pg_quit()
                    exit()
                    break

            else:
                display.update()
                continue

            break


class CrashScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.CRASH_BG, (0, 0))
        screen.blit(Constants.FONT.render("Press anywhere to quit!", True, Constants.BLACK),
                    (Constants.WINDOW_WIDTH / 2 - 180, Constants.WINDOW_HEIGHT / 1.15))

        while True:

            for event in pg_event.get():

                if event.type == QUIT or event.type == KEYDOWN:
                    pg_quit()
                    exit()
                    break

            else:
                display.update()
                continue

            break


class PauseScene(SceneBase):
    def __init__(self, current_level):
        SceneBase.__init__(self)
        self.current_level = current_level

    def render(self, screen):
        screen.blit(self.resources.PAUSE_BG, (0, 0))
        screen.blit(Constants.FONT.render("Press anywhere to resume!", True, Constants.BLACK),
                    (Constants.WINDOW_WIDTH / 2 - 198, Constants.WINDOW_HEIGHT / 1.15))

        while True:

            for event in pg_event.get():

                if event.type == QUIT:
                    pg_quit()
                    exit()

                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.switch_to_scene(self.current_level)
                    break

            else:
                display.update()
                continue

            break


class MidLevelScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.MIDLEVEL_BG, (0, 0))
        screen.blit(Constants.FONT.render("Next Level", True, Constants.BLACK),
                    (Constants.WINDOW_WIDTH / 2 - 60, Constants.WINDOW_HEIGHT / 2))
        display.update()
        sleep(4)


class FirstLevelScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        self.display_scrolling_background(screen, self.resources.FIRST_BG, 0.5)


class SecondLevelScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        self.display_scrolling_background(screen, self.resources.SECOND_BG, 1)


class ThirdLevelScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        self.display_scrolling_background(screen, self.resources.THIRD_BG, 1.5)
