from typing import Callable, Final
from platform import system


from .geometry import Size, Vector2, Coordinate

FPS: Final[int] = 60
EPS: float = 5
GAB: Final[int] = 10

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
VELOCITY: Final[Vector2] = Vector2(20, 20)
ACCELERATION: Final[Vector2] = Vector2(0.5, 0.5)


PEDAL_WIDTH: Final[int] = int(WIN_WIDTH / 10)
PEDAL_HEIGHT: Final[int] = int(WIN_HEIGHT / 70)
PEDAL_COORDINATES: Final[Coordinate] = Coordinate(
    int((WIN_WIDTH / 2) - (PEDAL_WIDTH / 2)), WIN_HEIGHT - PEDAL_HEIGHT * 4
)

BALL_WIDTH: Final[int] = int(WIN_WIDTH / 70)
BALL_HEIGHT: Final[int] = BALL_WIDTH
BALL_SIZE: Final[Size] = Size(BALL_WIDTH, BALL_HEIGHT)
BALL_VEL: Vector2 = Vector2(1, 1)
BALL_MAX_VEL: Vector2 = Vector2(20, 20)
BALL_COORDINATES: Callable[[int], Coordinate] = lambda i: Coordinate(  # noqa: E731
    GAB * 2, GAB * 16 + (GAB + BALL_HEIGHT) * i
)


COL: Final[int] = 3
ROW: Final[int] = 5
BALLS: Final[int] = 3

COLOR_LOWER: tuple[int, int, int] = (255, 0, 0)
COLOR_MID: tuple[int, int, int] = (0, 255, 0)
COLOR_UPPER: tuple[int, int, int] = (0, 0, 255)

if system() == "Linux":
    FONT: Final[str] = "JetBrains Mono Nerd Font"
    FONT_SIZE_SCORE: Final[int] = 38
    FONT_SIZE_END_MSG: Final[int] = 100
else:
    FONT: Final[str] = "JetBrainsMono NF SemiBold"  # type: ignore
    FONT_SIZE_SCORE: Final[int] = 20  # type: ignore
    FONT_SIZE_END_MSG: Final[int] = 60  # type: ignore
