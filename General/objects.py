from ._object import Object
from .camera import Camera
import pygame as pg
import sys


class Player:
    def __init__(self, x, y, keybind=None):
        self.x = x
        self.y = y
        self.camera: Camera = None
        self.keybind = keybind
    
    def attach_camera(self, camera) -> None:
        self.camera = camera

    def update(self, grid):
        if self.camera is not None:
            self.camera.update(grid, self.x, self.y)
        else:
            raise Exception

    def move(self):
        for event in pg.event.get():
            if event == pg.QUIT:
                pg.exit()
                sys.exit(1)






class Air(Object):
    def __init__(self, x, y):
        super().__init__(x, y, False, True, "engine/General/Air.png")

class Test(Object):
    def __init__(self):
        super().__init__(0, 0, False, True, "engine/General/test.png")
