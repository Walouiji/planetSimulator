from Planet import Planet
import pygame

running = True
planets = []
src = pygame.display.set_mode((500, 500))
while running:  
    pygame.init()
    print(pygame.mouse.get_pos()[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            planet = Planet(src, pygame.mouse.get_pos())
            circle = planet.draw_planet(src, pygame.mouse.get_pos())
            planets.append(circle)
    pygame.display.flip()
    