import pygame
import random
import time

pygame.init()


screen_width = 1000
screen_height = 700


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")

background = pygame.image.load('rfrwfrwfwc.png').convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

running = True

block_size = 20

snake = [(100, 100)]  # single block



direction = (block_size, 0)  # moving along right side

clock = pygame.time.Clock()

food = (random.randint(0, screen_width // block_size - 1) * block_size,
        random.randint(0, screen_height // block_size - 1) * block_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-block_size, 0)

            elif event.key == pygame.K_RIGHT:
                direction = (block_size, 0)

            elif event.key == pygame.K_DOWN:
                direction = (0, block_size)

            elif event.key == pygame.K_UP:
                direction = (0, -block_size)

    screen.blit(background, (0, 0))


    new_pos = (snake[0][0] + direction[0], snake[0][1] + direction[1])# tuple
    # snake[0] = new_pos # tuple


    # pygame.draw.rect(screen, snake_color, (snake[0][0], snake[0][1], block_size, block_size))

    # Check for collisions
    if (new_pos in snake or
            new_pos[0] < 0 or new_pos[0] >= screen_width or
            new_pos[1] < 0 or new_pos[1] >=screen_height):
        running = False  # Game over

    snake.insert(0, new_pos)

    if new_pos == food:

        food = (random.randint(0, screen_width // block_size- 1) *block_size,
                random.randint(0, screen_height // block_size - 1) * block_size)
    else:
        snake.pop()  # Remove tail if no food eaten

    for block in snake:
        pygame.draw.rect(screen, 'black',(block[0],block[1],block_size,block_size))




    pygame.draw.rect(screen, 'red', (food[0], food[1], block_size, block_size))


    pygame.display.flip()
    clock.tick(10)



