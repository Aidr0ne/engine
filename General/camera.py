import pygame as pg
import sys

class Camera:
    def __init__(self, distance, width, height, fullscreen=False):
        self.distance = distance
        if fullscreen:
            flags = pg.HWSURFACE | pg.FULLSCREEN | pg.SHOWN
        else: flags = pg.SHOWN

        pg.init()
        self.screen = pg.display.set_mode((width, height), flags)
        self.clock = pg.time.Clock()

    def update(self, grid, x, y):
        grid.update()
        for event in pg.event.get():
            if event == pg.QUIT:
                sys.exit(1)

        d = self.distance // 2

        # TODO: RENDER GRID
                            

        self.screen.fill("white")

        pg.display.flip()
        global dt
        dt = self.clock.tick(60) / 1000

        