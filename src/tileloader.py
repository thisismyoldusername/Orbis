#!/usr/local/bin/python3

"""Create instances of Tile class, read from tiles.config
So that mapmaker can just use bla.image for each bla
in a config file containing map data.
"""

# Import modules

import pygame
import pygame.locals
import configparser
from configparser import SafeConfigParser
import os
import re
import sprites

# Global vars

tiles_names = []
tiles_pos = []
texts = []

# Classes

class Tile:
    def __init__(self,mapname,name,pos):
        self.name = name
        self.pos = pos
        parser = configparser.SafeConfigParser()
        parser.read(mapname + '.tiles')
        self.image = parser.get(name,'image')
        self.block = parser.get(name,'block')
        tiles_names.append(self.name)
        tiles_pos.append(self.pos)

class Text:
    def __init__(self,content,status=False):
        self.content = content
        self.status = status
        texts.append(self)
        self.original = bla.copy()
        if self.status:
            self.show()

    def show(self):
        font = pygame.font.Font(None, 20)
        text = font.render(self.content, 1, (255,255,255))
        textpos = (50,430)
        bla.blit(text, textpos)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                bla.blit(self.original,(0,0))
                break
            

# Global functions

def filecount(directory):
    return len([f for f in os.listdir(directory)])


def make_tiles(tileset):
    bla = 1
    names = []
    images = []
    blocks = []
    amount = filecount('tiles/' + tileset)
    amount -= 1
    while bla <= amount:
        new_tile = Tile(tileset,str(bla),(0,0))
        names.append(new_tile.name)
        images.append(new_tile.image)
        blocks.append(new_tile.block)
        bla += 1
    return names, images, blocks



def print_tile(mapname,tile,loc):
    index = names.index(tile)
    tileobj = Tile(mapname,tile,loc)
    image = pygame.image.load(tileobj.image)
    screen.blit(image,loc)


def load_level(tilename,mapname):
    parser = configparser.SafeConfigParser()
    parser.read('levels.map')
    level = parser.get('level',tilename)
    return level

# http://pygame.org/docs/tut/chimp/ChimpLineByLine.html

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = 'sound/' + name
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Cannot load sound')
        raise SystemExit
    return sound

def print_text(content, background, textpos):
    font = pygame.font.Font(None, 20)
    text = font.render(content, 1, (255,255,255))
    bla.blit(text, textpos)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            bla.blit(background,(0,0))
            pygame.display.flip()
            return


def print_level(tilename,mapname,tile_width,tile_height):
    bla1 = 0
    bla2 = 0
    bla3 = (bla1,bla2)
    level = load_level(tilename,mapname)
    level_list = level.split('\t')
    amount_increase = 0
    for number in level_list:
        bla3 = (bla1,bla2)
        if number != ' ':
            if '\n' not in number:
                print_tile(mapname,number,bla3)
                bla1 += tile_width
                amount_increase += 1
            elif '\n' in number:
                number = number.split('\n')
                print_tile(mapname,number[0],bla3)
                bla2 += tile_height
                bla1 -= (amount_increase * tile_width)
                amount_increase = 0
                bla3 = (bla1,bla2)
                print_tile(mapname,number[1],bla3)
                bla1 += tile_width
                amount_increase += 1


# Actual code


if __name__ == '__main__':
    choice = input('What would you like your class to be?\n(Mage, Warrior, Archer)\n')
    choice = choice.upper()
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Orbis')

    if choice.startswith('M'):
        names, images, blocks = make_tiles('tileset')
        print_level('map5','tileset',24,16)
        pygame.display.flip()
        npc = pygame.image.load('sprites/smr1_fr1_b.gif').convert()
        screen.blit(npc,(108,10))
        pygame.display.flip()
        bla = screen.copy()
        print_text('Father: It is hard for someone like you to adapt to the',screen,(250,10))
        print_text('harsh life we have. If you had lived a thousand years ago,',screen,(250,25))
        print_text('you would have been a priest or a counselor of the king.',screen,(250,40))
        print_text('Now, there are few of you. A mage is rare, especially in',screen,(250,55))
        print_text('these lands. Not many understand you, and in your life',screen,(250,70))
        print_text('you will come across many men and women who will be',screen,(250,85))
        print_text('scared of you. This summer, you will become a man, and',screen,(250,100))
        print_text('yet there is much for you to learn. However, I am afraid',screen,(250,115))
        print_text('my shaman nor me can teach you more than you know',screen,(250,130))
        print_text('already. Therefore, I will send you to Graeca, a minor',screen,(250,145))
        print_text('city, only five days from now. There...what was that?',screen,(250,160))
        print_text('Soldier: Milord, we are under attack!',screen,(250,195))
        print_text('Father: By whom?',screen,(250,210))
        print_text('Soldier: I... I don\'t know sir. I have never seen',screen,(250,225))
        print_text('these kind of weapons, nor their crest.',screen,(250,240))
        char = sprites.Character((120,100),(24,16),'scr1_bk1_b.gif',75,50,75,150,75,'tileset')
        pygame.display.flip()
        sprites.event_loop((char),char,screen,bla,tiles_pos,tiles_names,texts)


    elif choice.startswith('W'):
        names, images, blocks = make_tiles('interior')
        print_level('map6','interior',24,16)
        pygame.display.flip()
        npc = pygame.image.load('sprites/mst1_lf2_b.gif').convert()
        screen.blit(npc,(155,100))
        pygame.display.flip()
        bla = screen.copy()
        print_text('Father: You have the blood of the ancient kings in your',screen,(250,10))
        print_text('veins. you truly are a warrior, deadly with a blade and',screen,(250,25))
        print_text('fearless. One day you will become the most feared warrior',screen,(250,40))
        print_text('of the plains, and you will bring peace and victory to',screen,(250,55))
        print_text('our tribe. Before that day is here, you must obtain a',screen,(250,70))
        print_text('blade worthy of your skills.',screen,(250,85))
        print_text('If I could, I\'d have the dwarfs make you one. However,',screen,(250,100))
        print_text('as you know, the dwarfs refuse to make anything for men',screen,(250,115))
        print_text('these days. Therefore, we\'ll have to make one ourselves.',screen,(250,130))
        print_text('I will send you to Graeca to get everything you will need',screen,(250,145))
        print_text('for a fine blade. Prepare for a five-day journey.',screen,(250,160))
        print_text('Go and... what was that?',screen,(250,175))
        print_text('Soldier: Incoming!',screen,(250,210))
        print_text('Father: What is happening?',screen,(250,225))
        print_text('Soldier: Enemy attack! Hideous creatures... I don\'t',screen,(250,240))
        print_text('know what they are...',screen,(250,255))
        char = sprites.Character((100,100),(24,16),'knt2_rt1_b.gif',100,100,75,20,75,'tileset')
        pygame.display.flip()
        sprites.event_loop((char),char,screen,bla,tiles_pos,tiles_names,texts)


    elif choice.startswith('A'):
        names, images, blocks = make_tiles('tileset')
        print_level('map7','tileset',24,16)
        pygame.display.flip()
        npc = pygame.image.load('sprites/ftr4_fr1_b.gif').convert()
        screen.blit(npc,(108,10))
        pygame.display.flip()
        bla = screen.copy()
        print_text('Father: With your hawk-like eyes and your killer instinct,',screen,(250,10))
        print_text('you will be the most feared hunter and assassin of our',screen,(250,25))
        print_text('time! At least as good as a wood-elf, probably better.',screen,(250,40))
        print_text('You can train the younglings and we can have a great',screen,(250,55))
        print_text('advantage upon the other tribes.',screen,(250,70))
        print_text('Yes, son. With masters of bow and sword we will strike',screen,(250,85))
        print_text('down our foes, and we will rule the lands once again.',screen,(250,100))
        print_text('Before we can begin, you will need to go to Graeca and',screen,(250,115))
        print_text('retrieve a bow I have ordered to make for you. Then, ',screen,(250,130))
        print_text('you are... in the name of God, what is that?!',screen,(250,145))
        print_text('Soldier: *grunt* Sire... Undead... Everywhere!',screen,(250,175))
        char = sprites.Character((120,100),(24,16),'mnv2_bk1_b.gif',75,75,75,50,150,'tileset')
        pygame.display.flip()
        sprites.event_loop((char),char,screen,bla,tiles_pos,tiles_names,texts)

    else:
        print('Something went wrong.')




