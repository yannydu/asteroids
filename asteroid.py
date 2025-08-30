import pygame
import random
from circleshape import CircleShape
from constants import *

# Class for asteroids

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2 

    def stick(self, other):
        bigger, smaller = (self, other) if self.radius >= other.radius else (other, self)
        bigger.radius += smaller.radius / 10
        smaller.kill()
            
        

        

