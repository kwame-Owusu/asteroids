from constants import *
from player import Player
import pygame


myPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main() -> None:
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  delta_time = 0
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    black_color = (0,0,0)
    screen.fill(color=black_color)
    delta_time = clock.tick(60) / 1000

    myPlayer.update(delta_time)
    myPlayer.draw(screen)
    pygame.display.flip()
    
 

if __name__ == "__main__":
  main()