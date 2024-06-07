import pygame
import math
import random
from entities.bodyparts.body import BodySquarePool


class Creature:
    def __init__(self, x, y, size, num_legs, colour):
        self.body_square_pool = BodySquarePool(20)  # NOTE 20 max set
        self.active = False
        self.x = x
        self.y = y
        self.size = size
        self.num_legs = num_legs
        self.speed_x = self.num_legs
        self.speed_y = self.num_legs
        self.colour = colour
        self.base_structure = self.body_square_pool.get_unused_body_square()
        self.base_structure.add_connection('b', self.body_square_pool.get_unused_body_square())
        self.base_structure.add_connection('t', self.body_square_pool.get_unused_body_square())
        self.base_structure.add_connection('r', self.body_square_pool.get_unused_body_square())
        self.base_structure.add_connection('l', self.body_square_pool.get_unused_body_square())

    def draw(self, screen):
        # Draw the creature's body
        self.base_structure.draw(screen, 'red', self.x, self.y, self.size)
        return

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def move(self):
        self.x += self.speed_x / 3
        self.y += self.speed_y / 3

    def check_collision(self, food):
        distance = math.hypot(self.x - food.x, self.y - food.y)
        return distance < self.size + food.size

# Creature pool
class CreaturePool:
    def __init__(self, capacity, screen_width, screen_height):
        self.pool = [
            Creature(
                random.randint(0, screen_width),
                random.randint(0, screen_height),
                size=10, num_legs=5,
                colour='red'
            )
            for _ in range(capacity)
        ]
