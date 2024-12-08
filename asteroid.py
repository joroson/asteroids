import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y , radius)

    def draw(self, screen):
        color = "white"
        width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        # asteroid_1.velocity *= 1.2
        asteroid_1.velocity = self.velocity.rotate(angle)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        # asteroid_2.velocity *= 1.2
        asteroid_2.velocity = self.velocity.rotate(-angle)