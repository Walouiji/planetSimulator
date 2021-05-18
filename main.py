from Planet import Planet
import pygame

running = True

src = pygame.display.set_mode((500, 500))
while running:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            circ = Planet(src, pygame.mouse.get_pos())
            print(event.type)
    pygame.display.flip()
    