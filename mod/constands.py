from typing import Final

from .geometry import Vector2, Coordinate

FPS: Final[int] = 60

WIN_WIDTH: Final[int] = 1000
WIN_HEIGHT: Final[int] = 600

RECT_SIZE_WIDTH_LIMITS: Final[Vector2] = Vector2(10, int(WIN_WIDTH / 3))
RECT_SIZE_HEIGHT_LIMITS: Final[Vector2] = Vector2(10, int(WIN_HEIGHT / 3))
RECT_POSITION_X_LIMITS: Final[Vector2] = Vector2(0, WIN_WIDTH - RECT_SIZE_WIDTH_LIMITS.y)
RECT_POSITION_Y_LIMITS: Final[Vector2] = Vector2(0, WIN_HEIGHT - RECT_SIZE_HEIGHT_LIMITS.y)

VELOCITY_REDUCE_FACTOR: Final[float] = 0.5
MIN_VELOCITY_THRESHOLD: Final[float] = 0.8

SPEED: Final[int] = 10
GRAVITY: Vector2 = Vector2(0, 0.5)
VELOCITY: Final[Vector2] = Vector2(-1, -1)
VELOCITY_2: Final[Vector2] = Vector2(1, 1)
ACCELERATION: Final[Vector2] = Vector2(0, 1)


PEDAL_SIZE_WIDTH: Final[int] = 200
PEDAL_SIZE_HEIGHT: Final[int] = 20
PEDAL_COORDINATES: Final[Coordinate] = Coordinate(
    int((WIN_WIDTH / 2) - (PEDAL_SIZE_WIDTH / 2)), WIN_HEIGHT - PEDAL_SIZE_HEIGHT * 2
)

MOVING_OBJ_WIDTH: Final[int] = 20
MOVING_OBJ_HEIGHT: Final[int] = 20
MOVING_OBJ_COORDINATES: Final[Coordinate] = Coordinate(
    int((WIN_WIDTH / 2) - (MOVING_OBJ_WIDTH / 2)), WIN_HEIGHT - MOVING_OBJ_HEIGHT * 2
)

STATIC_OBJ_WIDTH: Final[int] = 50
STATIC_OBJ_HEIGHT: Final[int] = 25

GAB: Final[int] = 20
