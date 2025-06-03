import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while(True):
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                return
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
