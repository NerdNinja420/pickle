import pygame
from pygame import Surface


# from .geometry import Vector2
from .circle import Circle
from .color import Color

from .constands import ACCELERATION, GRAVITY, VELOCITY_REDUCE_FACTOR


class Game:
    def __init__(self, surface: Surface, obj_count: int, choosen: Circle | None = None) -> None:
        self.surface = surface
        self.objects = [Circle.rand() for _ in range(obj_count)]
        self.choosen = choosen if choosen is not None else self.objects[0]
        self.choosen.color = Color.CHOSEN

    def bg(self):
        self.surface.fill(Color.BASE.rgb())

    def add_obj(self):
        self.objects.append(Circle.rand())

    def motion(self):
        for obj in self.objects:
            obj.handle_collision()
            obj.uniform()

    def reduce_velocity(self):
        for obj in self.objects:
            obj.reduce_vel(VELOCITY_REDUCE_FACTOR)

    def acceleration(self):
        for obj in self.objects:
            obj.accelerate(ACCELERATION)

    def gravitation(self):
        for obj in self.objects:
            obj.accelerate(GRAVITY)
            print(obj.vel.abs())

    def render(self):
        for object in self.objects:
            object.draw(self.surface)
        pygame.display.update()

    def handle_collision(self):
        for _ in range(len(self.objects)):
            for obj in self.objects:
                for other in self.objects:
                    dist_vector = obj.center - other.center
                    distance = dist_vector.abs()
                    if distance < 100 and distance > 0:
                        direction_vector = dist_vector / distance
                        obj.vel += direction_vector * 0.1
                        other.vel -= direction_vector * 0.1

    # def handle_input(self):
