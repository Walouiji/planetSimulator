import pygame
import random

class Planet:
    def __init__(self, Surface, position) -> None:
        self.RedGreenBlue = [(255,0,0),(0,255,0),(0,0,255)]
        self.PlanetSize = random.randint(10, 50)
        self.PlanetMass = self.PlanetSize * 5

        #Planet drawing
        #Planet.draw_planet(position.x, position.y, Surface, RedGreenBlue, self.PlanetSize)
        print(position[0])
        
        #gravity drawing
        gravity = pygame.draw.circle(Surface, (255,255,255), position, self.PlanetSize+(self.PlanetSize*2), width=1)
    
    def set_velocity(planet):
        planet.planet[0] += 10
        pass

    def draw_planet(Surface, positionX, positionY):
        RedGreenBlue = [(255,0,0),(0,255,0),(0,0,255)]
        planet = pygame.draw.circle(Surface, RedGreenBlue[random.randint(0,2)], positionX, positionY, 10, width=15)
        pass