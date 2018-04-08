def generate_graph(self, ):
  if self.A == 20:
    x_min = 0
    x_max = 3
    y_min = 0
    y_max = 4

  if self.A == 200:
    x_min = 0
    x_max = 7
    y_min = 0
    y_max = 24

  candidates = list(zip([i for i in range(x_min + 1, x_max)],
                        [i for i in range(y_min + 1, y_max)]))
