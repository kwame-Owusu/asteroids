from Shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_SPRINT_SPEED
import pygame

class Player(CircleShape):
  containers = ()
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.timer = 0
    self.points = 0
    
  
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
  
  def draw(self, screen: pygame.Surface) -> None:
    pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
     
  def rotate(self,delta_time: int) -> None:
    """
    rotate the player object by a delta time
    """
    self.rotation += PLAYER_TURN_SPEED * delta_time
  
  def update(self, delta_time: int) -> None:
    """
    updating the player position
    holding the key pressing logic using WASD
    """
    keys = pygame.key.get_pressed()
    self.timer -= delta_time
    speed_multiplier = 2 if keys[pygame.K_LSHIFT] else 1
    
    if keys[pygame.K_a]:
       self.rotate(-delta_time) 
    if keys[pygame.K_d]:
       self.rotate(delta_time)
    
    if keys[pygame.K_w]:
      self.move(delta_time, speed_multiplier) 
    if keys[pygame.K_s]:
      self.move(-delta_time, speed_multiplier) 
      
    if keys[pygame.K_SPACE]:
      if self.timer > 0:
        return
      self.shoot()
  
  def move(self, delta_time: int, speed_multiplier: float = 1.0) -> None:
    """
    method to allow player to move forward or backwards
    """
    forward = pygame.Vector2(0,1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * speed_multiplier * delta_time
    
  def shoot(self) -> None:
    self.timer = PLAYER_SHOOT_COOLDOWN
    new_shot = Shot(self.position.x, self.position.y)
    new_shot.velocity = pygame.math.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED 