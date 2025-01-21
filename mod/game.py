import pygame
from pygame import Surface


# from .geometry import Vector2
from .rectangle import Rectangle
from .geometry import Size, Vector2
from .color import Color

from .constands import (
    PEDAL_WIDTH,
    PEDAL_HEIGHT,
    PEDAL_COORDINATES,
    MOVING_OBJ_WIDTH,
    MOVING_OBJ_HEIGHT,
    MOVING_OBJ_COORDINATES,
    VELOCITY_2,
    WIN_WIDTH,
)


class Game:
    def __init__(self, surface: Surface, row: int, col: int) -> None:
        self.surface = surface
        self.static_objects = Rectangle.static(row, col)
        self.pedal_object = Rectangle(
            PEDAL_COORDINATES, Size(PEDAL_WIDTH, PEDAL_HEIGHT), Color.CHOSEN
        )
        self.moving_object = Rectangle(
            MOVING_OBJ_COORDINATES,
            Size(MOVING_OBJ_WIDTH, MOVING_OBJ_HEIGHT),
            Color.rand(),
            Vector2(10, 10),
        )

    def bg(self):
        self.surface.fill(Color.BASE.rgb())

    def motion(self):
        self.moving_object.uniform()
        self.pedal_object.uniform()

        self.moving_object.handle_collision()

    def handle_collision(self):
        if (
            self.moving_object.coordinates.y + self.moving_object.dimensions.height
            >= self.pedal_object.coordinates.y
            and self.moving_object.coordinates.x + self.moving_object.dimensions.width
            < self.pedal_object.coordinates.x + self.pedal_object.dimensions.width
            and self.moving_object.coordinates.x > self.pedal_object.coordinates.x
        ):
            self.moving_object.vel.y = -self.moving_object.vel.y

    def render(self):
        for object in self.static_objects:
            object.draw(self.surface)

        self.pedal_object.draw(self.surface)
        self.moving_object.draw(self.surface)

        pygame.display.update()

    def handle_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            if self.pedal_object.coordinates.x > 0:
                self.pedal_object.coordinates.x -= VELOCITY_2.x
        if key[pygame.K_d]:
            if self.pedal_object.coordinates.x + self.pedal_object.dimensions.width < WIN_WIDTH:
                self.pedal_object.coordinates.x += VELOCITY_2.x
