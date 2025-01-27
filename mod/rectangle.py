from __future__ import annotations
from typing import Callable

import pygame
from pygame import Surface

from .geometry import Coordinate, Size, Vector2
from .color import Color
from .constands import (
    RECT_SIZE_WIDTH_LIMITS,
    RECT_SIZE_HEIGHT_LIMITS,
    RECT_POSITION_X_LIMITS,
    RECT_POSITION_Y_LIMITS,
    WIN_HEIGHT,
    WIN_WIDTH,
    GAB,
)

Key = pygame.key.ScancodeWrapper


class Rectangle:
    def __init__(
        self,
        coordinates: Coordinate,
        size: Size,
        color: Color | tuple[int, int, int],
        vel: Vector2 | None = None,
    ) -> None:
        self.coord = coordinates
        self.dim = size
        self.color = color
        self.vel = vel if vel is not None else Vector2(0, 0)

    def __str__(self) -> str:
        return (
            f"Rectangle(x='{self.coord.x}', " + f"y='{self.coord.y}', " + f"color='{self.color}')"
        )

    def draw(self, surface: Surface):
        pygame.draw.rect(
            surface,
            (*self.color,),
            (*self.coord, *self.dim),
        )

    # TODO : draw the line from the corner pointing in the direction of velocity!
    def draw_vel_vec(self, surface: Surface):
        pygame.draw.line(
            surface,
            (*Color.TEXT,),
            (*self.coord,),
            (*(self.coord + self.vel * 200),),
        )

    print(*((1, 2, 3),))

    def uniform(self, delta: float):
        self.coord = self.coord + (self.vel * delta)

    def accelerate(self, acce: Vector2, same_dir: bool):
        if same_dir:
            self.vel = self.vel + self.vel.normalize() * acce.abs()
        else:
            self.vel = self.vel + acce

    def handle_collision_screen(self):
        if not (0 <= self.coord.x + self.vel.x <= WIN_WIDTH - self.dim.x):
            self.vel.x = -self.vel.x
        if not (0 <= self.coord.y + self.vel.y <= WIN_HEIGHT - self.dim.y):
            self.vel.y = -self.vel.y

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
    def static(
        cls,
        row: int,
        col: int,
        color_limits: list[tuple[int, int, int]] | None = None,
    ) -> list[Rectangle]:

        WIDTH: int = int((WIN_WIDTH - (GAB * (row + 1))) / row)
        HEIGHT: int = int(WIDTH * 0.15)
        COLORS = (
            [[Color.rand() for _ in range(row)] for _ in range(col)]
            if not color_limits
            else Color.range(color_limits, row * col, row)
        )

        x: Callable[[int], int] = lambda i: (GAB + WIDTH) * i + GAB  # noqa: E731
        y: Callable[[int], int] = lambda j: (GAB + HEIGHT) * j + GAB  # noqa: E731

        return [
            Rectangle(
                Coordinate(x(i), y(j)),
                Size(WIDTH, HEIGHT),
                COLORS[j][i],
            )
            for j in range(col)
            for i in range(WIN_WIDTH // (WIDTH + GAB))
        ]
