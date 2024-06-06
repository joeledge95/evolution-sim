import pygame
import sys
import random
from entities.creature import CreaturePool
from entities.habitat import Habitat
from entities.food import FoodPool

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
background_color = pygame.Color('green')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Instantiate creature pool
creature_pool = CreaturePool(2, screen_width, screen_height)

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

    # Draw habitat
    habitat.draw(screen)

    # All creature interractions
    for creature in creature_pool.pool:
        # Change direction if hit side
        if creature.x > screen_width or creature.x < 0:
            creature.speed_x *= -1
        if creature.y > screen_height or creature.y < 0:
            creature.speed_y *= -1
        # Move and Draw the creature
        creature.move()
        creature.draw(screen)
        # Handle food being eaten
        for food in food_pool.pool:
            if food.active and creature.check_collision(food):
                food.deactivate()
                creature.size += food.size

    # Draw food
    for food in food_pool.pool:
        food.draw(screen)

    # Logic to activate/deactivate food
    if random.randint(0, 100) > 95:  # Random chance to activate a food
        food_pool.activate_food(screen_width, screen_height)
    if random.randint(0, 100) > 98:  # Random chance to deactivate a food
        food_pool.deactivate_food()

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
