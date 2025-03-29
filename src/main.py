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
    
    # Text rendering setup (moved outside the loop)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        black_color = (0,0,0)
        screen.fill(color=black_color)
        delta_time = clock.tick(60) / 1000
        updatable.update(delta_time)
       
        # Render points text OUTSIDE of the collision loop
        points_text = font.render(f"Points: {myPlayer.points}", True, WHITE)
        points_rect = points_text.get_rect()
        points_rect.topleft = (10, 10)
        screen.blit(points_text, points_rect)

        
        if myPlayer.health <= 35:
            health_color = RED
        else:
            health_color = GREEN
        #render player health on game window
        health_text= font.render(f"Health: {myPlayer.health}", True, health_color)
        health_rect = health_text.get_rect()
        health_rect.topleft= (10, 40)
        screen.blit(health_text, health_rect)


        for asteroid in asteroids:
            if asteroid.has_collided(myPlayer):
                myPlayer.health -= 1   
                if myPlayer.health == 0:
                    print("Game Over!")
            for shot in shots:
                if asteroid.has_collided(shot):
                    shot.kill()
                    asteroid.split()
                    myPlayer.points += 10  # arbitrary number for points increase
        
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
    
 

if __name__ == "__main__":
  main()