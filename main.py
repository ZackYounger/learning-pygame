import pygame

from player import Player
from levelManager import levelManager

WIDTH = 1000
HEIGHT = 600
FPS = 60

## initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()


player = Player()
level_manager = levelManager()

gravity_strength = .8

## Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_q]:
        running = False

    screen.fill((0,0,0))

    player.update(keys_pressed, gravity_strength)
    player.draw(screen)

    pygame.display.flip()

pygame.quit()