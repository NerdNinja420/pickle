from typing import Final

from .geometry import Vector2, Coordinate

FPS: Final[int] = 60
EPS: float = 5

WIN_WIDTH: Final[int] = 1800
WIN_HEIGHT: Final[int] = 1000

RECT_SIZE_WIDTH_LIMITS: Final[Vector2] = Vector2(10, int(WIN_WIDTH / 3))
RECT_SIZE_HEIGHT_LIMITS: Final[Vector2] = Vector2(10, int(WIN_HEIGHT / 3))
RECT_POSITION_X_LIMITS: Final[Vector2] = Vector2(0, WIN_WIDTH - RECT_SIZE_WIDTH_LIMITS.y)
RECT_POSITION_Y_LIMITS: Final[Vector2] = Vector2(0, WIN_HEIGHT - RECT_SIZE_HEIGHT_LIMITS.y)

VELOCITY_REDUCE_FACTOR: Final[float] = 0.5
MIN_VELOCITY_THRESHOLD: Final[float] = 0.8

SPEED: Final[int] = 10
GRAVITY: Vector2 = Vector2(0, 0.5)
VELOCITY: Final[Vector2] = Vector2(30, 30)
ACCELERATION: Final[Vector2] = Vector2(0.5, 0.5)


PEDAL_WIDTH: Final[int] = int(WIN_WIDTH / 5)
PEDAL_HEIGHT: Final[int] = int(WIN_HEIGHT / 70)
PEDAL_COORDINATES: Final[Coordinate] = Coordinate(
    int((WIN_WIDTH / 2) - (PEDAL_WIDTH / 2)), WIN_HEIGHT - PEDAL_HEIGHT * 4
)

BALL_WIDTH: Final[int] = int(WIN_WIDTH / 70)
BALL_HEIGHT: Final[int] = BALL_WIDTH
BALL_VEL: Vector2 = Vector2(1, -1)
BALL_MAX_VEL: Vector2 = Vector2(10, 10)
BALL_COORDINATES: Final[Coordinate] = Coordinate(
    (WIN_WIDTH - (BALL_WIDTH // 2)) // 2, (WIN_HEIGHT - BALL_HEIGHT // 2) // 2
)

# STATICS_WIDTH: Final[int] = 30
# STATICS_HEIGHT: Final[int] = 25

GAB: Final[int] = 20
COL: Final[int] = 3
ROW: Final[int] = 5


COLOR_LOWER: tuple[int, int, int] = (255, 0, 0)
COLOR_MID: tuple[int, int, int] = (0, 255, 0)
COLOR_UPPER: tuple[int, int, int] = (0, 0, 255)
