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
    Shot.containers = (updatable, drawable)
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
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000 


if __name__ == "__main__":
    main()
