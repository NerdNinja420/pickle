import pygame
from pygame import KEYDOWN, Surface

from .rectangle import Rectangle
from .geometry import Size
from .color import Color

from .constands import (
    BALL_MIN_VEL,
    EPS,
    GAB,
    BALLS,
    WIN_WIDTH,
    WIN_HEIGHT,
    PEDAL_WIDTH,
    PEDAL_HEIGHT,
    PEDAL_COORDINATES,
    BALL_SIZE,
    BALL_START_VEL,
    BALL_MAX_VEL,
    BALL_COORDINATES,
    COLOR_MID,
    COLOR_LOWER,
    COLOR_UPPER,
    FONT,
    FONT_SIZE_SCORE,
    FONT_SIZE_END_MSG,
    VELOCITY,
    ACCELERATION,
)


class Game:
    def __init__(self, surface: Surface, row: int, col: int) -> None:
        self.surface = surface
        self.statics = Rectangle.static(
            row, col, (GAB * 12, GAB, GAB * 3), [COLOR_LOWER, COLOR_MID, COLOR_UPPER]
        )
        self.__ROW__ = row
        self.__COL__ = col
        self.pedal = Rectangle(
            PEDAL_COORDINATES,
            Size(PEDAL_WIDTH, PEDAL_HEIGHT),
            Color.CHOSEN,
        )
        self.balls = self.get_balls(BALLS)
        self.ball = self.balls[0]
        self.delta_time = 1
        self.score = 0
        self.h_s = 0
        self.lifes = 3

    def set_time(self, delta: float):
        self.time = delta

    def set_bg(self):
        self.surface.fill((*Color.BASE,))

    def get_balls(self, n: int) -> list[Rectangle]:
        return [
            Rectangle(
                BALL_COORDINATES(i),
                BALL_SIZE,
                Color.rand(),
                BALL_START_VEL.clone(),
            )
            for i in range(n)
        ]

    def motion(self):
        self.ball.uniform(self.delta_time)

    def restart(self):
        self.statics = Rectangle.static(
            self.__ROW__,
            self.__COL__,
            (GAB * 12, GAB, GAB * 3),
            [COLOR_LOWER, COLOR_MID, COLOR_UPPER],
        )
        self.pedal.coord = PEDAL_COORDINATES
        self.balls = self.get_balls(BALLS)
        self.ball = self.balls[0]
        self.h_s = self.score if self.score > self.h_s else self.h_s
        self.score = 0
        self.lifes = 3

    def pause(self, interval: int):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < interval * (10**3):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()

    def draw_status(self):
        font = pygame.font.SysFont(FONT, FONT_SIZE_SCORE)
        score = font.render(f"Score: {self.score}", True, Color.TEXT.rgb())
        self.surface.blit(score, (GAB, GAB))

        lifes = font.render(f"Lives: {self.lifes}", True, Color.TEXT.rgb())
        self.surface.blit(lifes, (GAB, GAB * 4))

        h_s = font.render(f"HS: {self.h_s}", True, Color.TEXT.rgb())
        self.surface.blit(h_s, (GAB + 5, GAB * 7))

    def draw_end_msg(self, won: bool):
        self.set_bg()

        msg = "Huraa! let's Go! you won!!!" if won else "You are out of lifes! :("

        font = pygame.font.SysFont(FONT, FONT_SIZE_END_MSG)
        text = font.render(msg, True, Color.TEXT.rgb())
        text_rect = text.get_rect(
            center=(
                self.surface.get_width() // 2,
                (self.surface.get_height() // 2) - (text.get_height() // 2),
            )
        )
        self.surface.blit(text, text_rect)

        score = font.render(f"Your score: {self.score}", True, Color.TEXT.rgb())
        self.surface.blit(score, (text_rect.x, text_rect.y + text_rect.height))

        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    elif event.key == pygame.K_SPACE:
                        self.restart()
                        running = False
                        break

    def render(self):
        self.set_bg()
        self.draw_status()

        for static in self.statics:
            static.draw(self.surface)
        for ball in self.balls:
            ball.draw(self.surface)
        self.pedal.draw(self.surface)

        pygame.display.update()

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
                self.score += 1

    def handle_score_life(self):
        if self.lifes == 0 and not len(self.statics) == 0:
            if len(self.balls) > 1:
                self.balls.remove(self.ball)
                self.ball = self.balls[0]
                self.lifes = 3
                self.pause(1)
            else:
                self.draw_end_msg(False)
        elif len(self.statics) == 0:
            self.draw_end_msg(True)

        if self.ball.coord.y + self.ball.vel.y + self.ball.dim.y >= WIN_HEIGHT:
            self.lifes -= 1

    def handle_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            if self.pedal.coord.x > -self.pedal.dim.w * 0.5:
                self.pedal.coord.x -= VELOCITY.x
        if key[pygame.K_d]:
            if self.pedal.coord.x + (self.pedal.dim.w * 0.5) < WIN_WIDTH:
                self.pedal.coord.x += VELOCITY.x

        if key[pygame.K_j]:
            if self.ball.vel.abs() <= BALL_MAX_VEL.abs():
                self.ball.accelerate(ACCELERATION, True)

        if key[pygame.K_k]:
            if self.ball.vel.abs() >= BALL_MIN_VEL.abs():
                self.ball.deaccelerate(ACCELERATION, True)

        # TODO: show a box with pop-up and fade-out animations
        if key[pygame.K_SPACE]:
            self.restart()

        if key[pygame.K_ESCAPE]:
            pygame.quit()
