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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


            try:
                chr(event.key)
            except:
                pass

    screen.fill("grey7")
    pygame.display.flip()
    clock.tick(180)

pygame.quit()
