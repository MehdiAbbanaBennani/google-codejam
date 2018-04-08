def neighbours(new_x, new_y):
    return [(x, y)
            for x in range(max(new_x - 1, 2), min(new_x + 2, 999))
            for y in range(max(new_y - 1, 2), min(new_y + 2, 999))]


def random_output(x, y) :
    neigh = neighbours(x, y)
    random_idx = np.random.choice(len(neigh), 1)
    return neigh[random_idx][0], neigh[random_idx][1]