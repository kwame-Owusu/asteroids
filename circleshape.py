import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # sub-classes must override
        pass 

    def update(self, dt: int) -> None:
        # sub-classes must override
        pass
    
    def has_collided(self, other_object: object) -> bool:
        """
        method to check for collisions, takes a CircleShape Object
        return True or False if collision happened with other object
        """
        distance_to_other = self.position.distance_to(other_object.position)
        if distance_to_other <= float(self.radius+ other_object.radius):
            return True
        return False
        
        