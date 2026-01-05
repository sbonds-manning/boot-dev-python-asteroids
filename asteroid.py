import pygame
from logger import log_event
from random import uniform

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        # Overloading the + means this is doing vector addition. Nice.
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        smaller_asteroid_angle_offset = uniform(20, 50)
        first_new_asteroid_direction = self.velocity.rotate(smaller_asteroid_angle_offset)
        second_new_asteroid_direction = self.velocity.rotate(-1*smaller_asteroid_angle_offset)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position.x,self.position.y,new_asteroid_radius)
        second_new_asteroid = Asteroid(self.position.x,self.position.y,new_asteroid_radius)

        first_new_asteroid.velocity = first_new_asteroid_direction * 1.2
        second_new_asteroid.velocity = second_new_asteroid_direction * 1.2