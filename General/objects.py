from ._object import Object
from .camera import Camera
import pygame as pg
import sys


class Player:
    def __init__(self, x, y, physics=False, sprite=None):
        self.x = x
        self.y = y
        self.name = "p"
        self.camera: Camera = None
        if sprite is not None:
            self.image = pg.image.load(sprite)
        else: self.image = None; print("Load fail")
        self.dt = 0
        self.input_delay = 0.1
        self.d = 0
        self.physics = physics

    def attach_camera(self, camera) -> None:
        self.camera = camera

    def physic(self, grid):  #TODO: FIX
        if self.physics == True:
            while True:
                if grid[self.x][self.y-1].solid == False:
                    self.y -= 1
                else: break


    def update(self, grid):
        running = True
        running = self.move()


        #print(self.x, self.y)
        #self.physic(grid)

        swp = grid[self.x][self.y]

        grid[self.x][self.y] = self
                
        if self.camera is not None:
            self.camera.update(grid, self.x, self.y)
        else:
            raise Exception
        
        grid[self.x][self.y] = swp
        
        self.dt = self.camera.dt
        return running

    def move(self):
        running = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        self.d += self.dt
        if self.d >= self.input_delay:
            keys = pg.key.get_pressed()
            if keys[pg.K_w]:
                self.x -= 1  # Fixed: Changed to -= to move up
                print("up")
            elif keys[pg.K_s]:
                self.x += 1  # Fixed: Changed to += to move down
            if keys[pg.K_a]:
                self.y -= 1  # Fixed: Changed to -= to move left
            elif keys[pg.K_d]:
                self.y += 1  # Fixed: Changed to += to move right
            self.d = 0
        return running





class Air(Object):
    def __init__(self, x, y):
        self.name = "A"
        super().__init__(x, y, False, True, "engine/General/Air.png")

class Test(Object):
    def __init__(self):
        self.name = "T"
        super().__init__(0, 0, False, True, "engine/General/test.png")

class Ground(Object):
    def __init__(self, x, y, solid=True, transparent=False, sprite=None, health=5):
        super().__init__(x, y, solid, transparent, sprite)
        self.health = health
        self.name = "G"