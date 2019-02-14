from pygame.draw import rect
from pygame import sysfont, KEYDOWN
from constants import Constants


class Button:

    def __init__(self, text, x, y, colour, colour_pressed, function, status, screen):

        self.status = status
        self.screen = screen
        self.colour = colour
        self.colour_pressed = colour_pressed
        self.x = x
        self.y = y
        self.function = function
        self.text = text
        self.font = sysfont.SysFont(Constants.FONT, 30)

        text_surf, text_rect = self.text_objects(Constants.BLACK)
        text_rect.center = ((x + (Constants.BUTTON_WIDTH / 2)), (y + (Constants.BUTTON_HEIGHT / 2)))
        self.screen.blit(text_surf, text_rect)

    def text_objects(self, colour):
        text_surface = self.font.render(self.text, True, colour)
        return text_surface, text_surface.get_rect()

    def update(self):

        if "selected" in self.status:
            rect(self.screen, self.colour, (self.x, self.y, Constants.BUTTON_WIDTH, Constants.BUTTON_HEIGHT))
        else:
            rect(self.screen, self.colour_pressed, (self.x, self.y, Constants.BUTTON_WIDTH, Constants.BUTTON_HEIGHT))

    def handle_event(self, event):

        if event.type == KEYDOWN and self.function is not None:
            self.function()
