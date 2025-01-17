class Chunk3D:
    def __init__(self):
        pass

class Chunk2D:
    def __init__(self):
        self.data = [[None for _ in range(16)] for _ in range(16)]

    def fill(self, filler):
        self.data = [[filler for _ in range(16)] for _ in range(16)]

    def get(self, x, y):
        return self.data[x][y]
    
class Zone3D:
    def __init__(self):
        self.data = [[Chunk2D() for _ in range(16)] for _ in range(16)]

    def fill(self, filler):
        for row in self.data:
            for chunk in row:
                chunk.fill(filler)