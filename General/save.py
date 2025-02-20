import pickle


def save_level(path, level):
    data = [[None for _ in range(len(level))] for _ in range(len(level[0]))]
    meta = [[None for _ in range(len(level))] for _ in range(len(level[0]))]
    for x in range(len(level)):
        for y in range(len(level[0])):
            data[x][y] = level[x][y].save()
            meta[x][y] = level[x][y].meta()

    with open(path, "wb") as file:
        pickle.dump(data, file)
    meta_path = path + ":meta"
    with open(meta_path, "wb") as file:
        pickle.dump(meta, file)


def load_level(path, save_dict):
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

    return level
