from engine.General._chunking import Zone2D

class Grid2D:
    def __init__(self, size, simulation_distance):
        self.grid = [[Zone2D() for _ in range(size)] for _ in range(size)]
        self.sim = simulation_distance

    def update(self, tx, ty):
        self.active = []
        for x in range(len(self.grid)):
            for y in range(x):
                if (x - 1 == tx) or (x == tx) or (x + 1 == tx) and (y - 1 == ty) or (y == ty) or (y + 1 == ty):
                    self.active.append(self.grid[x][y])

    def get_coords(self, x, y):
        zone_x = x // self.zone_size
        zone_y = y // self.zone_size

        # Calculate local position within the zone
        local_x = ((x % self.zone_size) + self.zone_size) % self.zone_size
        local_y = ((y % self.zone_size) + self.zone_size) % self.zone_size

        # Calculate chunk coordinates within the zone
        chunk_x = local_x // self.chunk_size
        chunk_y = local_y // self.chunk_size

        return zone_x, zone_y, chunk_x, chunk_y