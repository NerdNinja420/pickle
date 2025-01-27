from os import environ

from platform import system

import pygame
from pygame.locals import QUIT

from mod.game import Game
from mod.constands import FPS, WIN_WIDTH, WIN_HEIGHT

# environ["SDL_VIDEO_WINDOW_POS"] = "{},{}".format(-1650, 100)
# if system() == "Linux":
#     environ["SDL_VIDEO_WINDOW_POS"] = "{},{}".format(-1650, 100)
#


def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    CLOCK = pygame.time.Clock()

    game = Game(WIN, 10, 11)

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        # game.draw_end_msg()
        game.render()
        game.motion()
        game.handle_crash()
        game.handle_input()
        game.handle_score_life()
        game.handle_collision()

        game.set_time(delta=CLOCK.tick(FPS) / 1000)


if __name__ == "__main__":
    main()
