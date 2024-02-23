import pygame
import math


class Habitat:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen):
        # Calculate the vertices of the triangle
        # Assuming an equilateral triangle for simplicity
        height = math.sqrt(3) / 2 * self.size  # Height of the equilateral triangle
        vertex1 = (self.x, self.y - 2 / 3 * height)  # Top vertex
        vertex2 = (self.x - self.size / 2, self.y + 1 / 3 * height)  # Bottom left vertex
        vertex3 = (self.x + self.size / 2, self.y + 1 / 3 * height)  # Bottom right vertex

        # Draw the triangle
        pygame.draw.polygon(screen, pygame.Color('purple'), [vertex1, vertex2, vertex3])
