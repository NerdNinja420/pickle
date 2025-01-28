import pygame
from pygame import Surface

from .rectangle import Rectangle
from .geometry import Size
from .color import Color

from .constands import (
    EPS,
    GAB,
    BALLS,
    WIN_WIDTH,
    WIN_HEIGHT,
    PEDAL_WIDTH,
    PEDAL_HEIGHT,
    PEDAL_COORDINATES,
    BALL_SIZE,
    BALL_VEL,
    BALL_MAX_VEL,
    BALL_COORDINATES,
    COLOR_MID,
    COLOR_LOWER,
    COLOR_UPPER,
    VELOCITY,
    ACCELERATION,
)


class Game:
    def __init__(self, surface: Surface, row: int, col: int) -> None:
        self.surface = surface
        self.statics = Rectangle.static(
            row, col, (GAB * 12, GAB, GAB * 3), [COLOR_LOWER, COLOR_MID, COLOR_UPPER]
        )
        self.pedal = Rectangle(
            PEDAL_COORDINATES,
            Size(PEDAL_WIDTH, PEDAL_HEIGHT),
            Color.CHOSEN,
        )
        self.balls = self.get_balls(BALLS)
        self.ball = self.balls[0]
        self.delta_time = 1
        self.score = 0
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
                BALL_VEL.clone(),
            )
            for i in range(n)
        ]

    def pause(self, stop: int):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()

    def motion(self):
        self.ball.uniform(self.delta_time)

    def draw_status(self):
        font = pygame.font.SysFont("JetBrains Mono Nerd Font", 38)
        score = font.render(f"Score: {self.score}", False, Color.TEXT.rgb())
        self.surface.blit(score, (GAB, GAB))

        lifes = font.render(f"Lives: {self.lifes}", False, Color.TEXT.rgb())
        self.surface.blit(lifes, (GAB, GAB * 4))

    def draw_end_msg(self):
        self.set_bg()

        font = pygame.font.SysFont("JetBrains Mono Nerd Font", 100)
        text = font.render("You are out of lifes!☹", False, Color.TEXT.rgb())
        text_rect = text.get_rect(
            center=(self.surface.get_width() // 2, self.surface.get_height() // 2)
        )

        self.surface.blit(text, text_rect)
        pygame.display.update()

        self.pause(3000)

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
        if self.lifes == 0:
            if len(self.balls) > 1:
                self.balls.remove(self.ball)
                self.ball = self.balls[0]
                self.lifes = 3
                self.pause(1)
            else:
                self.draw_end_msg()

        if self.ball.coord.y + self.ball.vel.y + self.ball.dim.y >= WIN_HEIGHT:
            self.lifes -= 1

    def handle_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            if self.pedal.coord.x > -self.pedal.dim.w * 0.5:
                self.pedal.coord.x -= VELOCITY.x
        elif key[pygame.K_d]:
            if self.pedal.coord.x + (self.pedal.dim.w * 0.5) < WIN_WIDTH:
                self.pedal.coord.x += VELOCITY.x

        elif key[pygame.K_f]:
            if self.ball.vel.abs() <= BALL_MAX_VEL.abs():
                self.ball.accelerate(ACCELERATION, True)

        elif key[pygame.K_ESCAPE]:
            pygame.quit()
