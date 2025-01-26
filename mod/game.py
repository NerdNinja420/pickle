import pygame
from pygame import Surface

from .rectangle import Rectangle
from .geometry import Size
from .color import Color

from .constands import (
    EPS,
    PEDAL_WIDTH,
    PEDAL_HEIGHT,
    PEDAL_COORDINATES,
    BALL_WIDTH,
    BALL_HEIGHT,
    BALL_VEL,
    BALL_MAX_VEL,
    BALL_COORDINATES,
    WIN_WIDTH,
    VELOCITY,
    ACCELERATION,
)


class Game:
    def __init__(self, surface: Surface, row: int, col: int) -> None:
        self.surface = surface
        self.statics = Rectangle.static(row, col)
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
        self.surface.fill(Color.BASE.rgb())

    def motion(self):
        print(self.ball.vel)
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

    def is_colloding_to_side(self, a: Rectangle, b: Rectangle) -> bool:
        if a.coord.x >= b.coord.x + b.dim.w or a.coord.x + a.dim.w <= b.coord.x:
            return True
        return False

    # TODO : for higher precision collision handling take the velocity also into account!
    def handle_collision(self):
        self.ball.handle_collision_screen()

        if self.is_colliding(self.ball, self.pedal):
            self.pedal.color = Color.RED
            self.ball.color = Color.RED
            if self.is_colloding_to_side(self.ball, self.pedal):
                self.ball.vel.x = -self.ball.vel.x
            else:
                self.ball.vel.y = -self.ball.vel.y
        else:
            self.pedal.color = Color.CHOSEN
            self.ball.color = Color.CHOSEN

    # TODO : draw the line from the corner pointing in the direction of velocity!
    def render(self):
        for object in self.statics:
            object.draw(self.surface)

        self.pedal.draw(self.surface)
        self.ball.draw(self.surface)
        # pygame.draw.line(
        #     self.surface,
        #     Color.RED.rgb(),
        #     (*self.ball.coord,),
        #     (*(self.ball.coord + self.ball.vel * 200),),
        # )

        pygame.display.update()

    def handle_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            if self.pedal.coord.x > -self.pedal.dim.w * 0.5:
                self.pedal.coord.x -= VELOCITY.x
        if key[pygame.K_d]:
            if self.pedal.coord.x + (self.pedal.dim.w * 0.5) < WIN_WIDTH:
                self.pedal.coord.x += VELOCITY.x
        if key[pygame.K_SPACE]:
            if self.ball.vel.abs() <= BALL_MAX_VEL.abs():
                self.ball.accelerate(ACCELERATION, True)

        # if key[pygame.K_a]:
        #     self.ball.coord.x -= VELOCITY.x
        # if key[pygame.K_d]:
        #     self.ball.coord.x += VELOCITY.x
        # if key[pygame.K_w]:
        #     self.ball.coord.y -= VELOCITY.y
        # if key[pygame.K_s]:
        #     self.ball.coord.y += VELOCITY.y
