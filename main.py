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

## Game loop
running = True
while running:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,0,0), [100,100,100,100])

    pygame.display.flip()       

pygame.quit()