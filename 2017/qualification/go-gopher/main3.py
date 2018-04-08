import sys

candidates = [(x, y)
              for x in range(4, 5)
              for y in range(4, 6)]
loop_interact = True


def check_input(x, y):
    if x == 0 and y == 0:
        inter = False
        loop_inter = True
    elif x == -1 and y == -1:
        loop_inter = False
        inter = False
    else :
        inter = True
        loop_inter = True
    return inter, loop_inter


t = int(input().strip())
for i in range(1, t + 1):
    A = int(input().strip())
    while True:
        print("{} {}".format(order[0], order[1]), flush=True)
        x, y = [int(s) for s in input().split(" ")]
        if x == -1 and y == -1 :
            break
    if x == -1 and y == -1:
        break
sys.exit(0)