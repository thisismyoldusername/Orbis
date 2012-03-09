#!/usr/local/bin/python3

"""Draw sprites to map
"""

# Import modules

import pygame
import pygame.locals
from pygame import *
import sys
import configparser
from configparser import SafeConfigParser

class Character(pygame.sprite.Sprite):
    def __init__(self,pos,speed,image,health,strength,power,magic,ranged,world):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load('sprites/' + image).convert()
        self.rect = self.image.get_rect()
        self.pos = pos
        image_name = image.split('_')
        self.image_base = image_name[0]
        self.world = world

    def update(self):
#        if direction == 'down':
#            self.pos == (self.pos[0] + self.speed[0],self.pos[1])
#            screen.blit(test.image,(self.pos))
#            pygame.transform.flip(screen,1,1)
        pos = self.pos
        self.rect.midtop = pos
#        self.rect.move_ip(5, 10)
        
    def move(self,direction,tiles_pos,tiles_names,sprites):
        pos = self.pos
        parser = configparser.SafeConfigParser()
#        parser.read('tiles.config')
        parser.read(self.world + '.tiles')
#        print('tiles_pos:',tiles_pos)
#        print('tiles_names:',tiles_names)


        if direction == 'down':
            pos = (pos[0],pos[1] + 50)
            target_pos = (pos[0],pos[0]+50,pos[1],pos[1]+50)
      #      target_pos = (pos[0],pos[0]+50,pos[1],pos[1]-50)
            for x in range(target_pos[0],target_pos[1]):
                for tile_x in tiles_pos:
                    if tile_x[0] == x:
                        global target_x
                        target_x = x
            for y in range(target_pos[2],target_pos[3]):
                for tile_y in tiles_pos:
                    if tile_y[1] == y:
                        global target_y
                        target_y = y
            target_pos = (target_x,target_y)
            index = tiles_pos.index(target_pos)
            target_tile_name = tiles_names[index]
            block = parser.get(target_tile_name,'block')
            allsprites = pygame.sprite.RenderPlain(sprites)
            self.image = pygame.image.load('sprites/' + self.image_base + '_fr1_b.gif')
            allsprites.update()
            if block != 'True':
                self.pos = (pos[0] - 25,pos[1])
                self.image = pygame.image.load('sprites/' + self.image_base + '_fr2_b.gif')
                allsprites.update()
                self.pos = (self.pos[0] + 25,self.pos[1])
                self.image = pygame.image.load('sprites/' + self.image_base + '_fr1_b.gif')
                allsprites.update()
        elif direction == 'up':
            pos = (pos[0],pos[1] - 50)
            target_pos = (pos[0],pos[0]+50,pos[1],pos[1]+50)
            for x in range(target_pos[0],target_pos[1]):
                for tile_x in tiles_pos:
                    if tile_x[0] == x:
                        global target_x
                        target_x = x
            for y in range(target_pos[2],target_pos[3]):
                for tile_y in tiles_pos:
                    if tile_y[1] == y:
                        global target_y
                        target_y = y
            target_pos = (target_x,target_y)
            index = tiles_pos.index(target_pos)
            target_tile_name = tiles_names[index]
            block = parser.get(target_tile_name,'block')
            allsprites = pygame.sprite.RenderPlain(sprites)
            self.image = pygame.image.load('sprites/' + self.image_base + '_bk1_b.gif')
            allsprites.update()
            if block != 'True':
                self.pos = (pos[0] - 25,pos[1])
                self.image = pygame.image.load('sprites/' + self.image_base + '_bk2_b.gif')
                allsprites.update()
                self.pos = (self.pos[0] + 25,self.pos[1])
                self.image = pygame.image.load('sprites/' + self.image_base + '_bk1_b.gif')
                allsprites.update()
        elif direction == 'left':
            pos = (pos[0] - 50,pos[1])
            target_pos = (pos[0],pos[0]+50,pos[1],pos[1] + 50)
            for x in range(target_pos[0],target_pos[1]):
                for tile_x in tiles_pos:
                    if tile_x[0] == x:
                        global target_x
                        target_x = x
            for y in range(target_pos[2],target_pos[3]):
                for tile_y in tiles_pos:
                    if tile_y[1] == y:
                        global target_y
                        target_y = y
            target_pos = (target_x,target_y)
            index = tiles_pos.index(target_pos)
            target_tile_name = tiles_names[index]
            block = parser.get(target_tile_name,'block')
            allsprites = pygame.sprite.RenderPlain(sprites)
            self.image = pygame.image.load('sprites/' + self.image_base + '_lf1_b.gif')
            allsprites.update()
            if block != 'True':
                self.pos = (pos[0] - 25,pos[1])
                self.image = pygame.image.load('sprites/' + self.image_base + '_lf2_b.gif')
                allsprites.update()
                self.pos = (self.pos[0] + 25,self.pos[1])
                self.image = pygame.image.load('sprites/' + self.image_base + '_lf1_b.gif')
                allsprites.update()
        elif direction == 'right':
            pos = (pos[0] + 50,pos[1])
            target_pos = (pos[0] - 25,pos[0]+25,pos[1],pos[1]+50)
            for x in range(target_pos[0],target_pos[1]):
                for tile_x in tiles_pos:
                    if tile_x[0] == x:
                        global target_x
                        target_x = x
            for y in range(target_pos[2],target_pos[3]):
                for tile_y in tiles_pos:
                    if tile_y[1] == y:
                        global target_y
                        target_y = y
            target_pos = (target_x,target_y)
            index = tiles_pos.index(target_pos)
            target_tile_name = tiles_names[index]
            block = parser.get(target_tile_name,'block')
            allsprites = pygame.sprite.RenderPlain(sprites)
            self.image = pygame.image.load('sprites/' + self.image_base + '_rt1_b.gif')
            allsprites.update()
            if block != 'True':
                self.pos = (pos[0] - 25,pos[1])
                self.image = pygame.image.load('sprites/' + self.image_base + '_rt2_b.gif')
                allsprites.update()
                self.pos = (self.pos[0] + 25,self.pos[1])
                self.image = pygame.image.load('sprites/' + self.image_base + '_rt1_b.gif')
                allsprites.update()



def event_loop(sprites,char,screen,bg,tiles_pos,tiles_names,texts):
    allsprites = pygame.sprite.RenderPlain(sprites)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                char.move('down',tiles_pos,tiles_names,sprites)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                char.move('up',tiles_pos,tiles_names,sprites)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                char.move('left',tiles_pos,tiles_names,sprites)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                char.move('right',tiles_pos,tiles_names,sprites)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                for line in texts:
                    if line.status == True:
                        line.status == False


        allsprites.update()
        background = pygame.Surface(screen.get_size())
        background.blit(bg,(0,0))
        background = background.convert()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    test = Character((0,0),(24,16),'test.png',100,100,100,100,100)
    pygame.display.flip()
    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill((0,0,0))
    event_loop((test),test,screen,background)
