import pygame
from constants import *

def main():
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    
    white = (255,255,255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(white)
        pygame.display.flip()

if __name__ == "__main__":
    main()
