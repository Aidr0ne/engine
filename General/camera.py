import pygame as pg
import random
import time

class Camera:
    def __init__(self, distance, width, height, blank, fullscreen=False):
        self.distance = distance
        if fullscreen:
            flags = pg.HWSURFACE | pg.FULLSCREEN | pg.SHOWN | pg.DOUBLEBUF
        else:
            flags = pg.SHOWN | pg.DOUBLEBUF

        pg.init()
        self.height = height
        self.width = width
        self.screen = pg.display.set_mode((width, height), flags)
        self.clock = pg.time.Clock()
        self.dt = None
        self.blank = blank

    def recenter(self, grid, x, y):
        size = self.distance
        if size % 2 == 0 or size < 1:
            raise ValueError("Size must be an odd positive integer (e.g., 3, 5, 7).")
        
        half_size = size // 2
        
        subgrid = [[self.blank(0, 0) for _ in range(size)] for _ in range(size)]
        
        for i in range(size):
            for j in range(size):
                grid_x = x - half_size + i
                grid_y = y - half_size + j
                
                if 0 <= grid_x < len(grid) and 0 <= grid_y < len(grid[0]):
                    subgrid[i][j] = grid[grid_x][grid_y]
        
        return subgrid
    

    def update(self, grid, x, y):
        self.screen.fill("white")
        render = self.recenter(grid, x, y)
        tile_size = self.width // self.distance  # Ensure uniform tile size

        for i in range(len(render)):
            for j in range(len(render[0])):
                if hasattr(render[i][j], 'image'):
                    self.screen.blit(
                        render[i][j].image,
                        (j * tile_size, i * tile_size)  # **Fix: Removed incorrect camera_x and camera_y offsets**
                    )

        pg.display.update()  # More stable than flip
        self.dt = self.clock.tick(60) / 1000

        
class background:
    def __init__(self, width, height, possible_strings, adjacency_rules):
        self.width = width
        self.height = height
        self.possible_strings = possible_strings
        self.adjacency_rules = adjacency_rules
        self.grid = [[set(possible_strings) for _ in range(width)] for _ in range(height)]

    def collapse(self):
        while any(len(cell) > 1 for row in self.grid for cell in row):
            self._collapse_lowest_entropy_cell()
            self._propagate_constraints()

    def _collapse_lowest_entropy_cell(self):
        min_entropy = float('inf')
        candidates = []
        
        for y in range(self.height):
            for x in range(self.width):
                if len(self.grid[y][x]) > 1:
                    entropy = len(self.grid[y][x])
                    if entropy < min_entropy:
                        min_entropy = entropy
                        candidates = [(x, y)]
                    elif entropy == min_entropy:
                        candidates.append((x, y))
        
        if candidates:
            x, y = random.choice(candidates)
            self.grid[y][x] = {random.choice(tuple(self.grid[y][x]))}
    
    def _propagate_constraints(self):
        changed = True
        while changed:
            changed = False
            for y in range(self.height):
                for x in range(self.width):
                    if len(self.grid[y][x]) == 1:
                        value = next(iter(self.grid[y][x]))
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.width and 0 <= ny < self.height:
                                allowed_neighbors = self.adjacency_rules.get(value, set())
                                old_possibilities = self.grid[ny][nx]
                                self.grid[ny][nx] &= allowed_neighbors
                                if old_possibilities != self.grid[ny][nx]:
                                    changed = True
    
    def display(self):
        for row in self.grid:
            print(" ".join(next(iter(cell)) for cell in row))


