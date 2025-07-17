import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("Notes")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

    screen.fill("greygrey77")
    pygame.display.flip()
    clock.tick(180)

pygame.quit()
