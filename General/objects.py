from ._object import Object
from .camera import Camera
import pygame as pg
import pickle


class Player:
    def __init__(self, x=0, y=0, physics=False, sprite=None):
        self.x = x  # X Position used for rendering ease of access
        self.y = y  # Y Position used for rendering ease of access
        self.name = "Player"  # Name for debugging purposes
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
        self.save_id = 1

    def save(self):
        return [
            self.name,
            self.save_id,
            self.sprite_path,
            self.x,
            self.y,
            self.dt,
            self.input_delay,
            self.d,
            self.physics,
        ]

    def meta(self):
        return [
            "Name",
            "Save Id",
            "Sprite Path",
            "x",
            "y",
            "dt",
            "input Delay",
            "Amount of dt passed For input check",
            "If physics are enabled",
        ]

    def load(self, args):
        self.name = args[0]
        self.save_id = args[1]
        self.x = args[2]
        self.y = args[3]
        self.sprite_path = args[4]
        self.dt = args[5]
        self.input_delay = args[6]
        self.d = args[7]
        self.physics = args[8]
        self.__setstate__()

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
        if self.physics:
            while True:
                if not grid[self.x][self.y - 1].solid:
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

    def move(self, grid):
        running = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        self.d += self.dt
        if self.d >= self.input_delay:
            keys = pg.key.get_pressed()

            if keys[pg.K_w]:
                if not grid[self.x - 1][self.y].solid:
                    self.x -= 1  # Fixed: Changed to -= to move up
                else:
                    grid[self.x - 1][self.y].hp -= 1
                    if grid[self.x - 1][self.y].hp == 0:
                        grid[self.x - 1][self.y] = Air()

            elif keys[pg.K_s]:
                if not grid[self.x + 1][self.y].solid:
                    self.x += 1  # Fixed: Changed to += to move down
                else:
                    grid[self.x + 1][self.y].hp -= 1
                    if grid[self.x + 1][self.y].hp == 0:
                        grid[self.x + 1][self.y] = Air()

            elif keys[pg.K_a]:
                if not grid[self.x][self.y - 1].solid:
                    self.y -= 1  # Fixed: Changed to -= to move left
                else:
                    grid[self.x][self.y - 1].hp -= 1
                    if grid[self.x][self.y - 1].hp == 0:
                        grid[self.x][self.y - 1] = Air()

            elif keys[pg.K_d]:
                if not grid[self.x][self.y + 1].solid:
                    self.y += 1  # Fixed: Changed to += to move right
                else:
                    grid[self.x][self.y + 1].hp -= 1
                    if grid[self.x][self.y + 1].hp == 0:
                        grid[self.x][self.y + 1] = Air()

            elif keys[pg.K_SPACE]:
                grid, self.x, self.y = grid[self.x][self.y].use(grid, self.x, self.y)

            self.d = 0
        return running, grid


class Air(Object):
    def __init__(self):
        self.name = "Air"
        self.sprite_path = "/home/aiden/Engine/engine/General/Air.png"
        super().__init__(0, 0, False, True, "/home/aiden/Engine/engine/General/Air.png")
        self.save_id = 2
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
        (
            self.name,
            self.save_id,
            self.sprite_path,
            self.hp,
            self.transparent,
            self.solid,
        ) = args
        self.__setstate__()

    def save(self):
        return [
            self.name,
            self.save_id,
            self.sprite_path,
            self.hp,
            self.transparent,
            self.solid,
        ]

    def meta(self):
        return ["Name", "Save Id", "Sprite Path", "Hp", "Transparent", "Solid"]

    def use(self, level, x, y):
        return level, x, y


class Test(Object):
    def __init__(self):
        self.name = "T"
        super().__init__(0, 0, False, True, "engine/General/test.png")
        self.save_id = 2
        self.sprite_path = "engine/General/test.png"
        self.hp = 0

    def save(self):
        return [
            self.name,
            self.save_id,
            self.sprite_path,
            self.hp,
            self.solid,
            self.transparent,
        ]

    def meta(self):
        return []

    def load(self, args):
        (
            self.name,
            self.save_id,
            self.sprite_path,
            self.hp,
            self.solid,
            self.transparent,
        ) = args
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

    def use(self, level, x, y):
        return level, x, y


class Ground(Object):
    def __init__(self, x=0, y=0, solid=True, transparent=False, sprite=None, health=5):
        super().__init__(x, y, solid, transparent, sprite)
        self.hp = health
        self.name = "Ground"
        self.save_id = 3
        self.sprite_path = sprite

    def save(self):
        return [
            self.name,
            self.save_id,
            self.sprite_path,
            self.hp,
            self.solid,
            self.transparent,
            self.x,
            self.y,
        ]

    def meta(self):
        return [
            "Name",
            "Save Id",
            "Sprite Path",
            "Hp",
            "Solid",
            "Transparent",
            "X",
            "Y",
        ]

    def load(self, args):
        (
            self.name,
            self.save_id,
            self.sprite_path,
            self.hp,
            self.solid,
            self.transparent,
            self.x,
            self.y,
        ) = args
        self.__setstate__()

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

    def use(self, level, x, y):
        return level, x, y


class Door:
    def __init__(
        self,
        name="Door",
        x=0,
        y=0,
        tx=0,
        ty=0,
        target_file="",
        sprite_path="",
        save_dict=None,
        locked=False,
    ):
        self.x = x
        self.y = y
        self.tx = tx
        self.ty = ty
        self.transparent = True
        self.target_file = target_file
        self.hp = 1000000000
        self.solid = False
        self.locked = locked
        self.sprite_path = sprite_path
        self.image = None
        self.save_id = 4
        self.name = name
        self.save_dict = save_dict

    def save(self):
        return [
            self.name,
            self.save_id,
            self.sprite_path,
            self.x,
            self.y,
            self.tx,
            self.ty,
            self.locked,
            self.hp,
            self.target_file,
            self.save_dict,
        ]

    def meta(self):
        return [
            "Name",
            "Save Id",
            "Sprite Path",
            "X",
            "Y",
            "Target X",
            "Target Y",
            "Locked",
            "Hp",
            "Target File",
            "Save dictionary",
        ]

    def load(self, args):
        (
            self.name,
            self.save_id,
            self.sprite_path,
            self.x,
            self.y,
            self.tx,
            self.ty,
            self.locked,
            self.hp,
            self.target_file,
            self.save_dict,
        ) = args
        self.__setstate__()

    def use(self, level, x, y):
        if not self.locked:
            path = self.target_file
            save_dict = self.save_dict
            with open(path, "rb") as file:
                data = pickle.load(file)
            level = [[None for _ in range(len(data))] for _ in range(len(data[0]))]
            for x in range(len(data)):
                for y in range(len(data[0])):
                    level[x][y] = save_dict[data[x][y][0]]
                    print(data[x][y])
                    i = save_dict[data[x][y][0]]()
                    i.load(data[x][y])
                    level[x][y] = i

            return level, self.tx, self.ty
        return level, x, y

    def __setstate__(self):
        if self.sprite_path is not None:
            self.image = pg.image.load(self.sprite_path)  # Player sprite
        else:
            self.image = None
            print("sprite load fail")
