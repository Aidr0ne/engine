import pickle

def save_level(path, level):
    save_dict = {}
    data = [[None for _ in range(len(level))] for _ in range(level[0])]
    for x in range(len(level)):
        for y in range(len(level[0])):
            data[x][y] = level[x][y].save()

    with open(path, 'wb') as file:
        pickle.dump(data, file)

def load_level(path, save_dict, items):
    with open(name, "rb") as file:
        data = pickle.load(file)
    level = [[None for _ in range(len(data))] for _ in range(len(data[0]))]
    for x in range(len(data)):
        for y in range(len(data[0])):
            level[x][y] = save_dict[data[x][y][0]
            level[x][y].load(data[x][y])
            


