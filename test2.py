import pygame

x_pos = 0
v = 0
clock = pygame.time.Clock()
pygame.init()
size = width, height = 1280, 400
screen = pygame.display.set_mode(size)
running = True
value = True
t = 0
pygame.display.flip()
pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
    t += clock.tick() / 1000
    a = 1
    if value:
        x_pos += v * t + (a * (t ** 2)) / 2
    else:
        x_pos -= v * t + (a * (t ** 2)) / 2
    if x_pos >= 1280:
        value = False
        t = 0
    elif x_pos <= 0:
        value = True
    pygame.display.flip()

pygame.quit()
