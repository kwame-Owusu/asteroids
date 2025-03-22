from constants import *
import pygame

def main():
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
    pygame.display.flip()
    
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
  main()