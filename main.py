from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot
import pygame



updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots,updatable, drawable)

myPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main() -> None:
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  delta_time = 0
  astroid_field = AsteroidField()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    black_color = (0,0,0)
    screen.fill(color=black_color)
    delta_time = clock.tick(60) / 1000

    updatable.update(delta_time) 
    
    #settings for text render for points
    WHITE = (255, 255, 255)
    font = pygame.font.Font(None, 36) 
    
    # Get the rect of the text surface for positioning
    
    # Position the text in the center of the screen
    for asteroid in asteroids:
      if asteroid.has_collided(myPlayer):
        print("Game Over!")

      for shot in shots:
        if asteroid.has_collided(shot):
          shot.kill()
          asteroid.split()
          myPlayer.points += 10 #arbitrary number for points increase
          text_surface = font.render(f"points: {myPlayer.points}", True, WHITE)
          text_rect = text_surface.get_rect()
          text_rect.topleft = (10,10)
          screen.blit(text_surface, text_rect)
          pygame.display.flip()
          print(f"points : {myPlayer.points}")


    for item in drawable:
      item.draw(screen)
    pygame.display.flip()
    
 

if __name__ == "__main__":
  main()