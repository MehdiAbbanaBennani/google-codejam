import itertools
import sys


class Gopher():
    def __init__(self, A):
        self.A = A
        self.max_x, self.max_y = self.initialize_coordinates()
        self.graph = self.generate_graph()
        self.digged = self.generate_graph()

        self.current_neighbours_limit = 0

        self.loop_iterator = self.generate_loop_iterator()

    def initialize_coordinates(self):
        if self.A == 20:
            return 4, 5
        if self.A == 200:
            return 8, 25

    def generate_loop_iterator(self):
        iterator = ((x, y) for x in range(1, self.max_x) for y in range(1, self.max_y))
        return itertools.cycle(iterator)

    def generate_graph(self):
        return [[0 for i in range(self.max_y)] for j in range(self.max_x)]

    def purge(self, new_x, new_y):
        if self.digged[new_x][new_y] == 0:
            for x, y in self.neighbours(new_x, new_y):
                self.graph[x][y] += 1

    def neighbours(self, new_x, new_y):
        return ((x, y)
                for x in range(max(new_x - 1, 0), min(new_x + 2, self.max_x))
                for y in range(max(new_y - 1, 0), min(new_y + 2, self.max_y)))

    def update_digged(self, new_x, new_y):
        self.digged[new_x][new_y] = 1

    def next_pick(self):
        current_idx = next(self.loop_iterator)
        curr_x, curr_y = current_idx[0], current_idx[1]

        while self.graph[curr_x][curr_y] > self.current_neighbours_limit:
            current_idx = next(self.loop_iterator)
            curr_x, curr_y = current_idx[0], current_idx[1]

            if current_idx == (1, 1):
                self.current_neighbours_limit += 1
                self.current_neighbours_limit = min(self.current_neighbours_limit, 8)
        return current_idx

    def predict(self, new_x, new_y):
        if new_x is not -2 and new_y is not -2 :
            new_x, new_y = self.shift(new_x, new_y, plus=False)
            self.purge(new_x, new_y)
            self.update_digged(new_x, new_y)
            x_pick, y_pick = self.next_pick()
            return self.shift(x_pick, y_pick, plus=True)
        else:
            return self.shift(1, 1, plus=True)

    @staticmethod
    def shift(new_x, new_y, plus):
        if plus:
            return new_x + 100, new_y + 100
        else:
            return new_x - 100, new_y - 100


t = int(input().strip())
for i in range(1, t + 1):
    A = int(input().strip())
    gopher = Gopher(A)
    x = -2
    y = -2
    while True:
        order = gopher.predict(x, y)
        print("{} {}".format(order[0], order[1]), flush=True)
        x, y = [int(s) for s in input().split(" ")]
        if (x == -1 and y == -1) or (x == 0 and y == 0):
            break
    if x == -1 and y == -1:
        break
sys.exit(0)
