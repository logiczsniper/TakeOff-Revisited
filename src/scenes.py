from abc import abstractmethod, ABC
from sys import exit
from time import sleep

from pygame import event as pg_event, display, QUIT, quit as pg_quit, MOUSEBUTTONDOWN

from constants import Constants
from resources import Resources


class SceneBase(ABC):
    """
    A class from which all types of scenes must inherit from.
    """

    def __init__(self):
        """ Gain access to resources. """
        self.next = self
        self.resources = Resources()

    @abstractmethod
    def render(self, screen):
        """
        All scenes must overwrite this method as they all must display some sort of image to the user.

        :param screen: the display to draw to.
        :type: Display
        """
        pass

    @staticmethod
    def display_static_background(screen, background, text, text_x):
        """
        Display a non-moving background with text.

        :param screen: display to draw on.
        :type: Display

        :param background: the resource of the background image to draw.
        :type: Surface

        :param text: the text to display.
        :type: str

        :param text_x: the x value for the position of the text.
        :type: int
        """

        screen.blit(background, (0, 0))
        screen.blit(Constants.FONT.render(text, True, Constants.BLACK),
                    (text_x, Constants.WINDOW_HEIGHT / 1.15))

    def switch_to_scene(self, next_scene):
        """
        Sets self.next to the given scene, which will be set as the games active scene at the next iteration of the
        update method.

        :param next_scene: the scene that will be set.
        """

        self.next = next_scene
        return True


class StaticScene(SceneBase):
    """
    A scene that has a static background and must stop the main game loop by iterating in its own while loop which this
    scene is active. Such scenes are Pause and Title scenes.
    """

    def __init__(self, background, text, text_x, on_click=None, current_level=None):
        """
        Sets many variables that determine the nature of the scene, i.e, makes this class able to become both a Quit
        scene and a Victory scene and more.

        :param background: the background image for this scene.
        :type: Surface

        :param text: the text to be displayed.
        :type: str

        :param text_x: the x value to the position of the text.
        :type: int

        :param on_click: what will be executed when this scene is active and the user clicks the mouse.
        :type: lambda

        :param current_level: the current level that the user is on- level one, two, or three. Only the Pause scene
        needs this information, so it is nullable.
        """

        super().__init__()
        self.text_x = text_x
        self.text = text
        self.background = background
        self.on_click = on_click
        self.current_level = current_level

    def set_on_click(self, value):
        """
        If the on_click method was not initialized when the scene was, it will be set using this method.

        :param value: the expression that will be executed when this scene is active and the user clicks the mouse.
        :type: lambda
        """

        self.on_click = value

    def render(self, screen):
        """
        Displays the background image and text, then loops to stop the main game loop temporarily. While looping, it
        checks for a mouse click. When clicked, the on_click lambda is run.

        :param screen: display to draw on.
        :type: Display
        """

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
    """
    A simple scene used only to pause the game for 4 seconds, notifying the user that they are about to go to the next
    level, while displaying a unique background image that will give the user a break.
    """

    def __init__(self):
        super().__init__()

    def render(self, screen):
        """
        Displays the background, sleeps the main thread hence stopping the game loop for 4 seconds while this background
        is displayed with the text.

        :param screen: display to draw on.
        :type: Display
        """

        self.display_static_background(screen, self.resources.MIDLEVEL_BG, "Next Level",
                                       Constants.WINDOW_WIDTH / 2 - 70)
        display.update()
        sleep(4)


class LevelScene(SceneBase):
    """
    A scene that has a scrolling background image- all of the three level scenes use this as the scene.
    """

    def __init__(self, background, scroll_speed):
        """
        Sets crucial variables for the scrolling background that differentiate each level.

        :param background: the background image for this scene.
        :type: Surface

        :param scroll_speed: the speed at which the background will scroll downwards. Increments with each level to
        capture the increment in difficulty.
        :type: int
        """

        super().__init__()
        self.background = background
        self.scroll_speed = scroll_speed
        self.y = 0

    def display_scrolling_background(self, screen, image, speed):
        """
        Display a downward scrolling background image.

        :param screen: display to draw on.
        :type: Display

        :param image: the background image resource.
        :type: Surface

        :param speed: the speed at which the image will scroll downwards.
        :type: int
        """

        rel_y = self.y % image.get_rect().height
        screen.blit(image, (0, rel_y - image.get_rect().height))
        if rel_y < Constants.WINDOW_HEIGHT:
            screen.blit(image, (0, rel_y))
        self.y += speed
        display.update()

    def render(self, screen):
        """
        Implements the above method.

        :param screen: the screen that the scrolling background will draw on.
        :type: Display
        """

        self.display_scrolling_background(screen, self.background, self.scroll_speed)
