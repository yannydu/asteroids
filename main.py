import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for game_object in drawable:
            game_object.draw(screen)
            
        # If any asteroid collides with player => game over!
        for asteroid in asteroids:
            # Check if asteroid collides with player
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

            # How to check if asteroid collides with another asteroid
           # others = [other for other in asteroids if other != asteroid]
           # for other in others:
           #     if asteroid.collision(other):
           #         asteroid.stick(other)

            # Check if shots land on asteroid
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000 


if __name__ == "__main__":
    main()
