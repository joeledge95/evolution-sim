import pygame
import sys
import random
from src.python.entities.creature import Creature
from src.python.entities.habitat import Habitat
from src.python.entities.food import FoodPool

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
background_color = pygame.Color('green')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Instantiate a creature
creature = Creature(screen_width // 2, screen_height // 2, size=10, num_legs=5, colour='red')

# Instantiate a habitat
habitat = Habitat(screen_width // 2, screen_height // 2, size=60)

# Instantiate food pool
food_pool = FoodPool(10)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background, and draw the ball
    screen.fill(background_color)

    # Change direction if hit side
    if creature.x > screen_width or creature.x < 0:
        creature.speed_x *= -1
    if creature.y > screen_height or creature.y < 0:
        creature.speed_y *= -1

    # Move and Draw the creature
    creature.move()
    creature.draw(screen)

    # Draw habitat
    habitat.draw(screen)

    # Draw food
    # Example logic to activate/deactivate food
    if random.randint(0, 100) > 95:  # Random chance to activate a food
        food_pool.activate_food(screen_width, screen_height)
    if random.randint(0, 100) > 98:  # Random chance to deactivate a food
        food_pool.deactivate_food()
    food_pool.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
