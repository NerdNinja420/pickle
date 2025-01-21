import pygame
from pygame import Surface


# from .geometry import Vector2
from .rectangle import Rectangle
from .geometry import Size, Vector2
from .color import Color

from .constands import (
    ACCELERATION,
    PEDAL_SIZE_WIDTH,
    PEDAL_SIZE_HEIGHT,
    PEDAL_COORDINATES,
    MOVING_OBJ_WIDTH,
    MOVING_OBJ_HEIGHT,
    MOVING_OBJ_COORDINATES,
)


class Game:
    def __init__(self, surface: Surface, col: int) -> None:
        self.surface = surface
        self.static_objects = Rectangle.static(col)
        self.pedal_object = Rectangle(
            PEDAL_COORDINATES,
            Size(PEDAL_SIZE_WIDTH, PEDAL_SIZE_HEIGHT),
            Color.rand(),
        )
        self.moving_object = Rectangle(
            MOVING_OBJ_COORDINATES,
            Size(MOVING_OBJ_WIDTH, MOVING_OBJ_HEIGHT),
            Color.rand(),
            Vector2(5, 5),
        )

    def bg(self):
        self.surface.fill(Color.BASE.rgb())

    def motion(self):
        self.moving_object.handle_collision()
        self.moving_object.uniform()

    def acceleration(self):
        self.pedal_object.accelerate(ACCELERATION)

    def render(self):
        for object in self.static_objects:
            object.draw(self.surface)
        self.pedal_object.draw(self.surface)
        self.moving_object.draw(self.surface)
        pygame.display.update()
