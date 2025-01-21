from __future__ import annotations

import pygame
from pygame import Surface

from .geometry import Coordinate, Size, Vector2
from .color import Color
from .constands import (
    RECT_SIZE_WIDTH_LIMITS,
    RECT_SIZE_HEIGHT_LIMITS,
    RECT_POSITION_X_LIMITS,
    RECT_POSITION_Y_LIMITS,
    # VELOCITY_REDUCE_FACTOR,
    MIN_VELOCITY_THRESHOLD,
    STATIC_OBJ_WIDTH,
    STATIC_OBJ_HEIGHT,
    WIN_HEIGHT,
    WIN_WIDTH,
    GAB,
)

Key = pygame.key.ScancodeWrapper


class Rectangle:
    def __init__(
        self, coordinates: Coordinate, size: Size, color: Color, vel: Vector2 | None = None
    ) -> None:
        self.coordinates = coordinates
        self.dimensions = size
        self.color = color
        self.vel = vel if vel is not None else Vector2(0, 0)

    def __str__(self) -> str:
        return (
            f"Rectangle(x='{self.coordinates.x}', "
            + f"y='{self.coordinates.y}', "
            + f"color='{self.color}')"
        )

    def draw(self, surface: Surface):
        pygame.draw.rect(
            surface,
            self.color.rgb(),
            (*self.coordinates, *self.dimensions),
        )

    def uniform(self):
        self.coordinates = self.coordinates + self.vel

    def accelerate(self, acce: Vector2):
        self.vel = self.vel + acce

    def handle_collision(self):
        if not (0 <= self.coordinates.x + self.vel.x <= WIN_WIDTH - self.dimensions.x):
            self.vel.x = -self.vel.x
        if not (0 <= self.coordinates.y + self.vel.y <= WIN_HEIGHT - self.dimensions.y):
            self.vel.y = -self.vel.y
            if self.vel.abs() < MIN_VELOCITY_THRESHOLD:
                self.vel.x = 0
                self.vel.y = 0

    @classmethod
    def rand(cls) -> Rectangle:
        # from random import choice

        while True:
            color = Color.rand()
            size = Size.rand(RECT_SIZE_WIDTH_LIMITS, RECT_SIZE_HEIGHT_LIMITS)
            coordinates = Coordinate.rand(RECT_POSITION_X_LIMITS, RECT_POSITION_Y_LIMITS)

            if color not in [Color.BASE, Color.CHOSEN]:
                return Rectangle(coordinates, size, Color.rand(), Vector2(0, 0))

    @classmethod
    def static(cls, col: int) -> list[Rectangle]:
        objects: list[Rectangle] = []
        for j in range(col):
            for i in range(int(WIN_WIDTH / (STATIC_OBJ_WIDTH + GAB))):
                x = (GAB + STATIC_OBJ_WIDTH) * i + GAB
                y = (GAB + STATIC_OBJ_HEIGHT) * j + GAB

                obj = Rectangle(
                    Coordinate(x, y),
                    Size(STATIC_OBJ_WIDTH, STATIC_OBJ_HEIGHT),
                    Color.rand(),
                )

                objects.append(obj)

        return objects
