import os
import pygame
from pygame.locals import QUIT

from mod.game import Game
from mod.constands import FPS, WIN_WIDTH, WIN_HEIGHT

# set the window position to a constant in hyprland
# os.environ["SDL_VIDEO_WINDOW_POS"] = "{},{}".format(200, 100)
os.environ["SDL_VIDEO_WINDOW_POS"] = "-1650,20"


def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    CLOCK = pygame.time.Clock()

    game = Game(WIN, 10, 5)

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        game.bg()
        game.render()
        game.motion()
        game.handle_input()
        game.handle_collision()

        game.set_time(delta=CLOCK.tick(FPS) / 1000)


if __name__ == "__main__":
    main()
