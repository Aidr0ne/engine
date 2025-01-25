from ._object import Object
from .camera import Camera

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.camera: Camera = None
    
    def attach_camera(self, camera):
        self.camera = camera

    def update(self, grid):
        if self.camera is not None:
            self.camera.update(grid, self.x, self.y)
        else:
            raise Exception



class Air(Object):
    def __init__(self, x, y):
        super().__init__(x, y, False, True, "engine/General/Air.png")

class Test(Object):
    def __init__(self):
        super().__init__(0, 0, False, True, "engine/General/test.png")