import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *
from BallGame.game_objects import Bar

def main(local = True, difficulty = 5):
    '''
    game loop
    :return: /
    '''
    #init
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("game")
    #init background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))
     #ball = Ball([-math.pi/2,difficulty])
    clock = pygame.time.Clock()
    game_items = []
    game_sprites = []
    if local:
        local_player = Bar()
        local_player_sprite = pygame.sprite.RenderPlain(local_player)
        game_items.append(local_player)
        game_sprites.append(local_player_sprite)

    #first blit
    screen.blit(background, (0,0))
    pygame.display.flip()

    while True:
        clock.tick(60) #MAX 60 FPS
        #input handling
        pass
        #MANUAL PLAYER UPDATE
        if local:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        local_player.move_left()
                    if event.key == K_RIGHT:
                        local_player.move_right()
                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        local_player.stand_still()
        #object render update

        for item in game_items:
            screen.blit(background,item.rect, item.rect)
            item.update()
        for sprite in game_sprites:
            sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
