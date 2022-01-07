import pygame
from pygame.locals import *


def draw_block():
    surface.fill((255, 255, 255))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    # draw the surface and colour
    surface = pygame.display.set_mode((500, 500))
    surface.fill((255, 255, 255))

    # draw the block
    block = pygame.image.load("resources/block.jpg").convert()
    block_x = 0
    block_y = 0
    surface.blit(block, (block_x, block_y))

    # update the surface
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False