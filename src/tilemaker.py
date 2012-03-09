#!/usr/local/bin/python3

"""Code for making a tiled map
Used openSubDir function from provided link
load_tile_table is mostly based on a tutorial, but has quite some alterations
"""

# Import modules

import pygame
import pygame.locals
import configparser
import os

# Global Vars

x_bla = 24
y_bla = 16

# http://code.activestate.com/recipes/577027-find-file-in-subdirectory/

def openSubDir(filename, subdirectory=''):
    if subdirectory:
        path = subdirectory
    else:
        path = os.getcwd()
    for root, dirs, names in os.walk(path):
        if filename in names:
            return os.path.join(root, filename)
    raise 'File not found'

# http://wiki.sheep.art.pl/Tiled%20Map%20in%20PyGame

def load_tile_table(name,width,height):
    image = pygame.image.load(name).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    randvar = 0
    for tile_x in range(0, int(image_width/width)):
        line = []
        tile_table.append(line)
        for tile_y in range(0,int(image_height/height)):
            rect = (tile_x * width, tile_y * height, width, height)

            randvar += 1
            pygame.image.save(image.subsurface(rect), 'tiles/' + bla2 + '/' + str(randvar) + '.png')

            line.append(image.subsurface(rect))

    return tile_table

def make_config(path):
    listing = os.listdir('tiles/'+ path)

    for blafile in listing:
        config_layout = """
[{0}]
image = {1}
block = {2}

""".format(blafile.strip('.png'),'tiles/' + path + '/' + blafile, False)
        configfile = open('{0}.tiles'.format(path),'a')
        configfile.write(config_layout)


if __name__ == '__main__':
    bla = input('What is your tileset? \n')
    bla2 = bla.strip('.png')
    try:
        os.mkdir('tiles/' + bla2)
    except OSError:
        print('Directory',bla2,'already exists!\nIf there were files in it, they were overwritten!')
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    screen.fill((255,255,255))
#    table = load_tile_table(openSubDir(bla,subdirectory='tilesets'),24,16)
    table = load_tile_table(openSubDir(bla,subdirectory='tilesets'),x_bla,y_bla)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile,(x * x_bla, y * y_bla))
#            screen.blit(tile,(x * 24, y * 16))
    pygame.display.flip()
    pygame.image.save(screen,'tiles/' + bla2 + '/' + bla2 + '.png')
#    while pygame.event.wait().type != pygame.locals.QUIT:
#        pass
    make_config(bla2)


    asdf = input('OK?')
    pygame.quit()




