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
    
    for asteroid in asteroids:
      if asteroid.has_collided(myPlayer):
        print("Game Over!")

      for shot in shots:
        if asteroid.has_collided(shot):
          shot.kill()
          asteroid.split()


    for item in drawable:
      item.draw(screen)
    pygame.display.flip()
    
 

if __name__ == "__main__":
  main()