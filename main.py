import os
import time
import pygame
from pygame.locals import QUIT

from mod.game import Game
from mod.constands import FPS, WIN_WIDTH, WIN_HEIGHT


def main():
    pygame.init()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "{},{}".format(200, 100)

    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    CLOCK = pygame.time.Clock()

    old = time.time()

    game = Game(WIN, 10)

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.KEYDOWN:
                game.add_obj()
    
        now = time.time()

        game.bg()
        game.render()
        game.motion()
        game.gravitation()
        game.handle_collision()

        if now - old > 1:
            old = now
            game.reduce_velocity()

        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()
