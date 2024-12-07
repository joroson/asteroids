import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print(updatable)
    for i in updatable:
        print(i.__dict__)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        # Draw all the things
        for drawing in drawable:
            drawing.draw(screen)
        # player.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

        # Update all the things
        # player.update(dt)
        for update in updatable:
            update.update(dt)


if __name__ == '__main__':
    main()
