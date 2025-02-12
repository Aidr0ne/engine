from ._object import Object
from .camera import Camera
import pygame as pg


class Player:
    def __init__(self, x, y, physics=False, sprite=None):
        self.x = x  # X Position used for rendering ease of access
        self.y = y  # Y Position used for rendering ease of access
        self.name = "p"  # Name for debugging purposes
        self.camera: Camera = None  # Camera class for rendering
        self.sprite_path = sprite
        if sprite is not None:
            self.image = pg.image.load(sprite)  # Player sprite
        else:
            self.image = None
            print("Player sprite load fail")
        self.dt = 0  # Delta time variable taken from the camera class
        self.input_delay = 0.1  # Amount of time between inputs
        self.d = 0  # Amount of time since last input check
        self.physics = physics  # If physics is enabled
        self.save_id = 0

    def __getstate__(self):
        self.image = None

    def __setstate__(self):
        if self.sprite_path is not None:
            self.image = pg.image.load(self.sprite_path)  # Player sprite
        else:
            self.image = None
            print("Player sprite load fail")

    def attach_camera(self, camera) -> None:
        self.camera = camera

    def physic(self, grid):  # TODO: FIX
        if self.physics == True:
            while True:
                if grid[self.x][self.y - 1].solid == False:
                    self.y -= 1
                else:
                    break

    def update(self, grid) -> bool:
        running = True
        running = self.move(grid)

        # print(self.x, self.y)
        # self.physic(grid)

        swp = grid[self.x][self.y]

        grid[self.x][self.y] = self

        if self.camera is not None:
            self.camera.update(grid, self.x, self.y)
        else:
            raise Exception

        grid[self.x][self.y] = swp

        self.dt = self.camera.dt
        return running

    def move(self, grid) -> bool:
        running = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        self.d += self.dt
        if self.d >= self.input_delay:
            keys = pg.key.get_pressed()

            if keys[pg.K_w] and grid[self.x - 1][self.y].solid == False:
                self.x -= 1  # Fixed: Changed to -= to move up
            else:
                grid[self.x - 1][self.y].hp -= 1
                if grid[self.x - 1][self.y].hp == 0:
                    grid[self.x - 1][self.y] = Air()

            if keys[pg.K_s] and grid[self.x + 1][self.y].solid == False:
                self.x += 1  # Fixed: Changed to += to move down
            else:
                grid[self.x + 1][self.y].hp -= 1
                if grid[self.x + 1][self.y].hp == 0:
                    grid[self.x + 1][self.y] = Air()

            if keys[pg.K_a] and grid[self.x][self.y - 1].solid == False:
                self.y -= 1  # Fixed: Changed to -= to move left
            else:
                grid[self.x][self.y - 1].hp -= 1
                if grid[self.x][self.y - 1].hp == 0:
                    grid[self.x][self.y - 1] = Air()

            if keys[pg.K_d] and grid[self.x][self.y + 1].solid == False:
                self.y += 1  # Fixed: Changed to += to move right
            else:
                grid[self.x][self.y + 1].hp -= 1
                if grid[self.x][self.y + 1].hp == 0:
                    grid[self.x][self.y + 1] = Air()
            self.d = 0
        return running


class Air(Object):
    def __init__(self):
        self.name = "Air"
        self.sprite_path = "engine/General/Air.png"
        super().__init__(0, 0, False, True, "engine/General/Air.png")
        self.save_id = 1
        self.solid = False
        self.hp = 0

    def __getstate__(self):
        self.image = None

    def __setstate__(self):
        if self.sprite_path is not None:
            self.image = pg.image.load(self.sprite_path)  # Player sprite
        else:
            self.image = None
            print("sprite load fail")

    def hit(self):
        self.hp -= 1

    def load(self, args):
        self.sprite_path, self.hp, self.transparent, self.solid, self.name = (
            args.split()
        )
        self.__setstate__()

    def save(self):
        return [self.sprite_path, self.hp, self.transparent, self.solid, self.name]


class Test(Object):
    def __init__(self):
        self.name = "T"
        super().__init__(0, 0, False, True, "engine/General/test.png")
        self.save_id = 2
        self.sprite_path = "engine/General/test.png"
        self.hp = 0

    def save(self):
        return [self.name, self.hp, self.solid, self.transparent, self.sprite_path]

    def load(self, args):
        self.name, self.hp, self.solid, self.transparent, self.sprite_path = (
            args.split()
        )
        self.__setstate__()

    def hit(self):
        self.hp -= 1

    def __getstate__(self):
        self.image = None

    def health(self):
        return self.hp

    def __setstate__(self):
        if self.sprite_path is not None:
            self.image = pg.image.load(self.sprite_path)  # Player sprite
        else:
            self.image = None
            print("sprite load fail")


class Ground(Object):
    def __init__(self, x, y, solid=True, transparent=False, sprite=None, health=5):
        super().__init__(x, y, solid, transparent, sprite)
        self.hp = health
        self.name = "G"
        self.save_id = 3
        self.sprite_path = sprite

    def save(self):
        return [self.name, self.hp, self.solid, self.transparent, self.x, self.y]

    def load(self, args):
        self.name, self.hp, self.solid, self.transparent, self.x, self.y = args.split()

    def __getstate__(self):
        self.image = None

    def __setstate__(self):
        if self.sprite_path is not None:
            self.image = pg.image.load(self.sprite_path)  # Player sprite
        else:
            self.image = None
            print("sprite load fail")

    def hit(self):
        self.hp -= 1

    def health(self):
        return self.hp
