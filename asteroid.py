from circleshape import CircleShape
import pygame


class Asteroid(CircleShape):
  containers = ()
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen: pygame.Surface) -> None:
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
  
  def update(self, delta_time: int) -> None:
    self.position += self.velocity * delta_time
      
  
  
  