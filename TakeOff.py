""" Recreating TakeOff

Logan Czernel
"""

from game import Game
from pygame import init, quit


if __name__ == "__main__":

    # Initialize pygame.
    init()

    # Create game.
    new_game = Game()

    # Run game.
    new_game.run()

    # Quit pygame.
    quit()
