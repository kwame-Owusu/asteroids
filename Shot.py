from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    containers = ()
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity
         
    
    def update(self, delta_time: int) -> None:
        # Move the shot based on its velocity
        self.position += self.velocity * delta_time
        
    def draw(self, screen: pygame.Surface) -> None:
        # Draw the shot as a circle
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)