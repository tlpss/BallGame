import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *
from game_objects import Bar, Ball

def main(local = True, difficulty = 5):
    '''
    game loop
    :return: 
    '''
    #init
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("game")
    #init background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))
    clock = pygame.time.Clock()
    game_items = []
    game_sprites = []
    if local:
        player = Bar()
        local_player_sprite = pygame.sprite.RenderPlain(player)
        game_items.append(player)
        game_sprites.append(local_player_sprite)
        ball = Ball([0,0],player)

    game_items.append(ball)
    ball_sprite = pygame.sprite.RenderPlain(ball)
    game_sprites.append(ball_sprite)
    #first blit
    screen.blit(background, (0,0))
    for sprite in game_sprites:
        sprite.draw(screen)
    pygame.display.flip()

    #INIT
    init = True
    while init:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                print("started")
                ball.vector = [math.pi/4*random.random()+0.2,difficulty]
                init = False
    #TODO: add and keep score
    while ball.alive:
        clock.tick(60) #MAX 60 FPS
        #MANUAL PLAYER UPDATE
        if local:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        player.move_left()
                    if event.key == K_RIGHT:
                        player.move_right()
                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        player.stand_still()
        #object render update

        for item in game_items:
            screen.blit(background,item.rect, item.rect)
            item.update()
        for sprite in game_sprites:
            sprite.draw(screen)

        pygame.display.flip()

    #TODO: if lost -> restart! (auto training)

if __name__ == "__main__":
    main()
