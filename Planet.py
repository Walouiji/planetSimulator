import pygame
import random

class Planet:
    def __init__(self, Surface, position) -> None:
        RedGreenBlue = [(255,0,0),(0,255,0),(0,0,255)]
        self.PlanetSize = random.randint(10, 50)
        self.PlanetMass = self.PlanetSize * 5

        #Planet drawing
        self.planet = pygame.draw.circle(Surface, RedGreenBlue[random.randint(0,2)], position, self.PlanetSize, width=self.PlanetSize)

        #gravity drawing
        gravity = pygame.draw.circle(Surface, (255,255,255), position, self.PlanetSize+(self.PlanetSize*2), width=1)
    
    def getMass(self):
        return self.PlanetMass
    
    def set_velocity(planet):
        planet.x += 10
        pass