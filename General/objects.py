from _object import Object

class Player:
    def __init__(self):
        global player_exists
        player_exists = True

    def close(self):
        global player_exists
        player_exists = False

class Air(Object):
    def __init__(self, x, y):
        super().__init__(x, y, False, True, "Air.png")