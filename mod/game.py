import pygame
from pygame import Surface

from .rectangle import Rectangle
from .geometry import Size
from .color import Color

from .constands import (
    COLOR_MID,
    EPS,
    WIN_WIDTH,
    PEDAL_WIDTH,
    PEDAL_HEIGHT,
    PEDAL_COORDINATES,
    BALL_WIDTH,
    BALL_HEIGHT,
    BALL_VEL,
    BALL_MAX_VEL,
    BALL_COORDINATES,
    COLOR_LOWER,
    COLOR_UPPER,
    VELOCITY,
    ACCELERATION,
)


class Game:
    def __init__(self, surface: Surface, row: int, col: int) -> None:
        self.surface = surface
        self.statics = Rectangle.static(row, col, [COLOR_LOWER, COLOR_MID, COLOR_UPPER])
        self.pedal = Rectangle(
            PEDAL_COORDINATES,
            Size(PEDAL_WIDTH, PEDAL_HEIGHT),
            Color.CHOSEN,
        )
        self.ball = Rectangle(
            BALL_COORDINATES,
            Size(BALL_WIDTH, BALL_HEIGHT),
            Color.rand(),
            BALL_VEL.clone(),
        )
        self.delta = 1

    def set_time(self, delta: float):
        self.time = delta

    def bg(self):
        self.surface.fill((*Color.BASE,))

    def render(self):
        for object in self.statics:
            object.draw(self.surface)

        self.pedal.draw(self.surface)
        self.ball.draw(self.surface)

        pygame.display.update()

    def motion(self):
        self.ball.uniform(self.delta)

    def is_colliding(self, a: Rectangle, b: Rectangle) -> bool:
        if (
            a.coord.y + a.dim.h + EPS > b.coord.y
            and a.coord.y - EPS < b.coord.y + b.dim.h
            and a.coord.x + a.dim.w + EPS > b.coord.x
            and a.coord.x - EPS < b.coord.x + b.dim.w
        ):
            return True
        return False

    def is_colliding_to_side(self, a: Rectangle, b: Rectangle) -> bool:
        if a.coord.x > b.coord.x + b.dim.w or a.coord.x + a.dim.w < b.coord.x:
            return True
        return False

    # TODO : take VELOCITY also into account!
    def handle_collision(self):
        self.ball.handle_collision_screen()

        if self.is_colliding(self.ball, self.pedal):
            self.pedal.color, self.ball.color = (Color.RED, Color.RED)
            if self.is_colliding_to_side(self.ball, self.pedal):
                self.ball.vel.x = -self.ball.vel.x
            else:
                self.ball.vel.y = -self.ball.vel.y
        else:
            self.pedal.color, self.ball.color = (Color.CHOSEN, Color.CHOSEN)

    def handle_crash(self):
        for static in self.statics:
            if self.is_colliding(self.ball, static):
                if self.is_colliding_to_side(self.ball, static):
                    self.ball.vel.x = -self.ball.vel.x
                else:
                    self.ball.vel.y = -self.ball.vel.y
                self.statics.remove(static)

    def handle_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            if self.pedal.coord.x > -self.pedal.dim.w * 0.5:
                self.pedal.coord.x -= VELOCITY.x
        elif key[pygame.K_d]:
            if self.pedal.coord.x + (self.pedal.dim.w * 0.5) < WIN_WIDTH:
                self.pedal.coord.x += VELOCITY.x
        elif key[pygame.K_SPACE]:
            if self.ball.vel.abs() <= BALL_MAX_VEL.abs():
                self.ball.accelerate(ACCELERATION, True)

        elif key[pygame.K_ESCAPE]:
            pygame.quit()

        # if key[pygame.K_a]:
        #     self.ball.coord.x -= VELOCITY.x
        # if key[pygame.K_d]:
        #     self.ball.coord.x += VELOCITY.x
        # if key[pygame.K_w]:
        #     self.ball.coord.y -= VELOCITY.y
        # if key[pygame.K_s]:
        #     self.ball.coord.y += VELOCITY.y
