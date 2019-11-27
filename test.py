import pygame
from random import randrange

x_pos = 0
v = 500
clock = pygame.time.Clock()
pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for i in range(5000):
        pygame.draw.rect(screen, pygame.Color('white'), (randrange(0, 300), randrange(0, 300), 1, 0),
                         0)
    pygame.display.flip()

pygame.init()
pygame.quit()
