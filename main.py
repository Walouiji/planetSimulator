from Planet import Planet
import pygame

running = True
planets = []
src = pygame.display.set_mode((500, 500))
while running:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            planets.append(Planet(src, pygame.mouse.get_pos()))
    for planet in planets:
        planet.planet.x += 100
        print(planet.planet.x)
    pygame.display.flip()
    