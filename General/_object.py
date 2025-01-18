import pygame as pg

class Object:
    def __init__(self, 
                 x, 
                 y, 
                 solid = True, 
                 transparent = False, 
                 sprite=None):
        self.x = x
        self.y = y
        self.solid = solid
        self.transparent = transparent
        if sprite is not None:
            self.sprite = pg.image.load(sprite)
        else: self.sprite = None