from os import path
import sys
from time import time_ns
import pygame

PIXEL_SCALE = int("4") if len(sys.argv) == 1 else int(sys.argv[1])
TILE_SCALE = 16

def main():
    pygame.init()

    # Load resources
    sleeping_dog1 = pygame.image.load(
        path.join("resources", "SleepingDogAnimated1.png")
        )
    sleeping_dog2 = pygame.image.load(
        path.join("resources", "SleepingDogAnimated2.png")
        )

    # Setup the window
    pygame.display.set_icon(sleeping_dog1)
    pygame.display.set_caption("Hello sir! :D")
    screen = pygame.display.set_mode((
                                      16 * TILE_SCALE * PIXEL_SCALE, 
                                      9  * TILE_SCALE * PIXEL_SCALE))

    # Game loop
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    main()