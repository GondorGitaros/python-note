import pygame

pygame.init()
pygame.display.set_caption("Notes")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
text = [""]
line = 0
column = 0
cursor = [line, column]
font = pygame.font.SysFont("Times New Roman", 30)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if text != [""]:
                    if (text[line] == "" and text != "" or column == 0 and line != 0):
                        if len(text[line]) == 0:
                            del text[line]
                        line-=1
                        column = len(text[line])
                        print(f"line: {line} column: {column}")
                    elif text[line] != "" and not (line == 0 and column == 0): 
                        text[line] = text[line][:column - 1] + text[line][column:]
                        column-=1
                        print(f"line: {line} column: {column}")

            elif event.key == pygame.K_RETURN:
                text.append("")
                line+=1
                column = 0
                cursor = [line, column]
                print(f"line: {line} column: {column}")

            elif event.key == pygame.K_LEFT:
                if not column <= 0:
                    column-=1
                    print(f"line: {line} column: {column}")
            elif event.key == pygame.K_RIGHT:
                if not column == len(text[line]):
                    column+=1
                    print(f"line: {line} column: {column}")
            elif event.key == pygame.K_UP:
                if not line <= 0:
                    line-=1
                    print(f"line: {line} column: {column}")
            elif event.key == pygame.K_DOWN:
                if not line + 1 == len(text):
                    line+=1
                    print(f"line: {line} column: {column}")

            else:
                try:
                    text[line] = text[line][:column] + (event.unicode) + text[line][column:]
                    column += 1
                    print(f"line: {line} column: {column}")
                except:
                    print("Not a key")

    screen.fill("grey7")

    for i in range(len(text)):
        text_surface = font.render(text[i], False, (255,255,255))
        screen.blit(text_surface, (3, i * 30))


    pygame.display.flip()
    clock.tick(180)

pygame.quit()
