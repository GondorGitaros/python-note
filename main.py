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
            if event.key == pygame.K_BACKSPACE:
                if line == 0 and text[0] == "":
                    print("Nothing to delete")
                    print(text)
                elif text[line] == "" and text != "":
                    text.pop()
                    line-=1
                if text[0] != "": 
                    text[line] = text[line][:-1]
                    print(text)

            elif event.key == pygame.K_RETURN:
                text.append("")
                line+=1
            else:
                try:
                    text[line] += (event.unicode)
                    print(text)
                except:
                    print("Not a key")

    screen.fill("grey7")

    for i in range(len(text)):
        text_surface = font.render(text[i], False, (255,255,255))
        screen.blit(text_surface, (3, i * 30))



    pygame.display.flip()
    clock.tick(180)

pygame.quit()
