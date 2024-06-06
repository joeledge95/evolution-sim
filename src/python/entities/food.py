import pygame
import random


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.active = False
        self.size = 5

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, pygame.Color('yellow'), (self.x, self.y), self.size)


# Food Pool
class FoodPool:
    def __init__(self, capacity):
        self.pool = [Food() for _ in range(capacity)]

    def activate_food(self, screen_width, screen_height):
        for food in self.pool:
            if not food.active:
                # Position food randomly within screen bounds
                food.x, food.y = (random.randint(0, screen_width), random.randint(0, screen_height))
                food.activate()
                break

    def deactivate_food(self):
        for food in self.pool:
            if food.active:
                food.deactivate()
                break

    def draw(self, screen):
        for food in self.pool:
            food.draw(screen)
