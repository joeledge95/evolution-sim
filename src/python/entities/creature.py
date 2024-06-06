import pygame
import math


class Creature:
    def __init__(self, x, y, size, num_legs, colour):
        self.x = x
        self.y = y
        self.size = size
        self.num_legs = num_legs
        self.speed_x = self.num_legs
        self.speed_y = self.num_legs
        self.colour = colour

    def draw(self, screen):
        # Draw the creature's body
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)
        # Draw the creature's legs
        leg_length = 20  # Increased leg length for visibility
        for i in range(self.num_legs):
            angle_degrees = (360 / self.num_legs) * i
            angle_radians = math.radians(angle_degrees)  # Convert degrees to radians
            leg_x = int(self.x + math.cos(angle_radians) * (self.size + leg_length))
            leg_y = int(self.y + math.sin(angle_radians) * (self.size + leg_length))
            pygame.draw.line(screen, self.colour, (self.x, self.y), (leg_x, leg_y), 2)

    def move(self):
        self.x += self.speed_x / 3
        self.y += self.speed_y / 3

    def check_collision(self, food):
        distance = math.hypot(self.x - food.x, self.y - food.y)
        return distance < self.size + food.size
