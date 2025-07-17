# python note taking app
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("Notes")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
text = [""]
line = 0
font = pygame.font.SysFont("Times New Roman", 30)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE:
                if text[line] != "":
                    text[line] = text[line][:-1]
                else:
                    print("Nothing to delete")
            else:
                try:
                    text[line] += (event.unicode)
                except:
                    print("Not a key")

    screen.fill("grey7")

    text_surface = font.render(text[line], False, (255,255,255))
    screen.blit(text_surface, (3,3))

    pygame.display.flip()
    clock.tick(180)

pygame.quit()
