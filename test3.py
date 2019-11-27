import pygame

x_pos = -600
v = 1280
clock = pygame.time.Clock()
pygame.init()
size = width, height = 1280, 400
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 4:
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 20)
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 20)
    pygame.display.flip()

pygame.quit()