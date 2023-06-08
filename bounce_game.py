import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bounce Game")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player_width = 100
player_height = 20
player_x = (width - player_width) // 2
player_y = height - player_height - 10
player_speed = 5

# Set up the ball
ball_radius = 10
ball_x = random.randint(ball_radius, width - ball_radius)
ball_y = random.randint(ball_radius, height // 2)
ball_speed_x = random.choice([-2, 2])
ball_speed_y = 2

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for ball collision with walls
    if ball_x < ball_radius or ball_x > width - ball_radius:
        ball_speed_x *= -1
    if ball_y < ball_radius:
        ball_speed_y *= -1

    # Check for ball collision with player
    if (
        ball_y + ball_radius >= player_y
        and player_x <= ball_x <= player_x + player_width
    ):
        ball_speed_y *= -1

    # Check if the ball went out of bounds
    if ball_y > height:
        # Reset the ball position
        ball_x = random.randint(ball_radius, width - ball_radius)
        ball_y = random.randint(ball_radius, height // 2)
        ball_speed_x = random.choice([-2, 2])
        ball_speed_y = 2

    # Clear the screen
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(
        window,
        WHITE,
        pygame.Rect(player_x, player_y, player_width, player_height)
    )

    # Draw the ball
    pygame.draw.circle(
        window,
        WHITE,
        (int(ball_x), int(ball_y)),
        ball_radius
    )

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
