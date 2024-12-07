import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # super().__init__(velocity)
        self.x_pos = x
        self.y_pos = y
        self.radius = radius

    def draw(self, screen):
        color = "white"
        width = 2
        pygame.draw.circle(screen, color, (self.x_pos, self.y_pos), self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt
