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
            self.image = pg.image.load(sprite)
        else: self.image = None; print("Load fail")

    def solid(self):
        return self.solid