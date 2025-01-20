from typing import Final

from .geometry import Vector2

FPS: Final[int] = 60

WIN_WIDTH: Final[int] = 1920
WIN_HEIGHT: Final[int] = 1200

CIRCLE_RADIUS_LIMITS: Final[Vector2] = Vector2(10, int(WIN_WIDTH / 6))
CIRCLE_POSITION_MIN_LIMITS: Final[Vector2] = Vector2(
    CIRCLE_RADIUS_LIMITS.y, WIN_WIDTH - (CIRCLE_RADIUS_LIMITS.x)
)
CIRCLE_POSITION_MAX_LIMITS: Final[Vector2] = Vector2(
    CIRCLE_RADIUS_LIMITS.x, WIN_HEIGHT - (CIRCLE_RADIUS_LIMITS.y)
)

VELOCITY_REDUCE_FACTOR: Final[float] = 0.5
MIN_VELOCITY_THRESHOLD: Final[float] = 0.8

SPEED: Final[int] = 10
GRAVITY: Vector2 = Vector2(0, 0.5)
VELOCITY: Final[Vector2] = Vector2(-1, -1)
VELOCITY_2: Final[Vector2] = Vector2(1, 1)
ACCELERATION: Final[Vector2] = Vector2(0, 1)
