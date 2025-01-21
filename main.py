import os
import pygame
from pygame.locals import QUIT

from mod.game import Game
from mod.constands import FPS, WIN_WIDTH, WIN_HEIGHT


def main():
    pygame.init()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "{},{}".format(200, 100)

    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    CLOCK = pygame.time.Clock()

    game = Game(WIN, 5)

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        game.bg()
        game.render()
        game.motion()

        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()
