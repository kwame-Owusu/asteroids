from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
import pygame

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
  
  def triangle(self) -> list[int]:
    """
    shape of the player class
    """
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen) -> None:
    pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
     
  def rotate(self,delta_time: int) -> None:
    """
    rotate the player object by a delta time
    """
    self.rotation += PLAYER_TURN_SPEED * delta_time
  
  def update(self, delta_time: int) -> None:
    """
    holding the key pressing logic using WASD
    """
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
       self.rotate(-delta_time) 
    if keys[pygame.K_d]:
       self.rotate(delta_time)
    
