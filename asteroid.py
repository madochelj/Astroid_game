import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, shot):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        shot.kill()

        angle = random.uniform(20, 50)
        NEW_VECTOR = self.velocity.rotate(angle)
        NEW_RADIUS = self.radius - ASTEROID_MIN_RADIUS
        new = Asteroid(self.position.x, self.position.y, NEW_RADIUS)
        new_2 = Asteroid(self.position.x, self.position.y, NEW_RADIUS)

        new.velocity = NEW_VECTOR * 1.2
        new_2.velocity = -NEW_VECTOR * 1.2

