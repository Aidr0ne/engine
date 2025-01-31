import pygame as pg
import sys

class Camera:
    def __init__(self, distance, width, height, fullscreen=False):
        self.distance = distance
        if fullscreen:
            flags = pg.HWSURFACE | pg.FULLSCREEN | pg.SHOWN | pg.DOUBLEBUF
        else: flags = pg.SHOWN | pg.DOUBLEBUF

        pg.init()
        self.height = height
        self.width = width
        self.screen = pg.display.set_mode((width, height), flags)
        self.clock = pg.time.Clock()

    def recenter(self, grid, x, y):
        self.grid = grid
        half_distance = self.distance // 2

        start_row = max(y - half_distance, 0)
        end_row = min(y + half_distance + 1, len(self.grid))
        start_col = max(x - half_distance, 0)
        end_col = min(x + half_distance + 1, len(self.grid[0]))

        return [row[start_col:end_col] for row in self.grid[start_row:end_row]]

    def update(self, grid, x, y):
            
        self.screen.fill("white")

        render = self.recenter(grid, x, y)
        for i in range(len(render)):
            for j in range(len(render[0])):
                if hasattr(render[i][j], 'image'):
                    self.screen.blit(
                        render[i][j].image,
                        (j * (self.width // self.distance), i * (self.height // self.distance))
                    )
                        

        pg.display.flip()
        global dt
        dt = self.clock.tick(60) / 1000

        
