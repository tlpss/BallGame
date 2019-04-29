import pygame
import math
from BallGame.resource_handling import Loader

#ALL RENDERED OBJECTS MUST INHERIT FROM SPRITE


class Ball(pygame.sprite.Sprite):
    '''
    simple ball object with internal position and velocity (ang cords)
    '''
    def __init__(self,vector,player):
        pygame.sprite.Sprite.__init__(self)
        self.image = Loader.load_png("ball_trans.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = player.rect.midtop
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.player = player
        self.alive = True

    def update(self):
        new_pos = self._calcnewpos(self.rect,self.vector)
        self.rect = new_pos
        (angle, speed) = self.vector

        #border collision detection
        if not (self.area.contains(new_pos)):
            print('border collision')
            #TODO: border collision
            #-> detect which border  (down -> lost,
            # right angle = pi - angle,
            # upper - > anlge + 2* pi -angle
            # left ...

        #player collision detection
        if self.player.rect.colliderect(new_pos):
            angle =  -angle
            self.vector = (angle,speed)


    def _calcnewpos(self,rect,vector):
        angle,speed = vector
        dx = speed * math.cos(angle)
        dy = speed * math.sin(angle)
        return rect.move(dx,dy)

class Bar(pygame.sprite.Sprite):
    states = {"moveleft": -1, "still" : 0, "moveright" : 1} #object states
    def __init__(self, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = Loader.load_png("bar.png")
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.midbottom = self.area.midbottom
        self.state = Bar.states.get("still")
        self.speed = speed #object's speed
        self.pos = [0,0]
        self.rect.bottom = self.area.bottom

    def move_left(self):
        self.pos[0] -= self.speed
        self.state = Bar.states.get("moveleft")

    def move_right(self):
        self.pos[0] += self.speed
        self.state = Bar.states.get("moveright")

    def stand_still(self):
        self.pos = [0,0]
        self.state = Bar.states.get("still")

    def update(self):
        new_pos = self.rect.move(self.pos)
        if self.area.contains(new_pos):
            self.rect = new_pos
        pygame.event.pump() #update event queue

