from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
  containers = ()
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
    
  def draw(self, screen: pygame.Surface) -> None:
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
  
  def update(self, delta_time: int) -> None:
    self.position += self.velocity * delta_time
  
  def split(self) -> None:
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    #spawn 2 new asteroids

    #randomize the angle of the split
    random_angle = random.uniform(20, 50)
    a = self.velocity.rotate(random_angle)
    b = self.velocity.rotate(-random_angle)

    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid.velocity = a * 1.2

    asteroid = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid.velocity = b * 1.2
    


      
  
  
  