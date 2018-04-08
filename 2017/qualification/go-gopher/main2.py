import sys

candidates = [(x, y)
              for x in range(4, 6)
              for y in range(4, 7)]

t = int(input().strip())
for i in range(1, t + 1):
    A = int(input().strip())
    it = 0
    while True:
        order = candidates[it % len(candidates)]
        print("{} {}".format(order[0], order[1]), flush=True)
        x, y = [int(s) for s in input().split(" ")]
        it += 1
        if (x == -1 and y == -1) or (x == 0 and y == 0):
            break
    if x == -1 and y == -1:
        break
sys.exit(0)