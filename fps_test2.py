import sys
from typing import Deque
import pygame
from pygame.locals import QUIT

pygame.init()
#　オブジェクトを作成
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()


def main():
    #main routine
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0
    while True:
        # SURFACE.fill((255, 255, 255)) 

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        counter += 1
        SURFACE.fill((0,0,0))
        counter_image = sysfont.render(
            'count is {}'.format(counter), True, (255, 255, 255)
        )
        SURFACE.blit(counter_image, (50, 50))
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()