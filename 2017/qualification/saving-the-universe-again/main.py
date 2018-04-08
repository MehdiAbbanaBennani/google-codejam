import math


def summarize(seq):
    summary = []

    current_count = 0
    prev_s = seq[0]

    for s in seq :
        if s == prev_s:
            current_count += 1
        else:
            summary.append((prev_s, current_count))
            prev_s = s
            current_count = 1
    if prev_s == "S" :
        summary.append((prev_s, current_count))

    return summary


def compute_damage(seq_summary):
    damage = 0
    charge = 1
    for element in seq_summary:
        if str(element[0]) == "S":
            damage += element[1] * charge
        else:
            charge *= 2 ** element[1]
    return damage


def min_damage(seq):
    return seq.count("S")


def compute_last_strength(seq_summary):
    return 2**sum([seq_summary[i][1] if seq_summary[i][0] == "C" else 0 for i in range(len(seq_summary))])


def count_last_s(seq_summary):
    assert seq_summary[-1][0] == "S"
    return seq_summary[-1][1]


def count_moves(seq_summary, delta):
    last_strength = compute_last_strength(seq_summary)
    last_s_count = count_last_s(seq_summary)

    if math.ceil(last_strength / 2)* last_s_count > delta:
        return math.ceil(delta / math.ceil(last_strength / 2)), seq_summary, True
    else:
        new_seq_summary = move_c(seq_summary)
        return last_s_count, new_seq_summary, False


def move_c(seq_summary):
    last = seq_summary.pop()
    before_last = seq_summary.pop()

    if before_last[1] == 1:
        if len(seq_summary) > 0:
            before_before = seq_summary.pop()
            seq_summary.append(("S", before_before[1] + last[1]))
        else:
            seq_summary.append(("S", last[1]))
    else:
        seq_summary.append(("C", before_last[1] - 1))
        seq_summary.append(("S", last[1]))
    return seq_summary


def min_hacks(seq_summary, d):
    moves = 0

    current_damage = compute_damage(seq_summary)
    delta = current_damage - d

    while delta > 0:
        new_moves, seq_summary, end = count_moves(seq_summary, delta)
        moves = moves + new_moves
        current_damage = compute_damage(seq_summary)
        delta = current_damage - d

        if end :
            delta = 0
    return moves


def save_the_universe(D, seq):
    minimum = min_damage(seq)
    seq_summary = summarize(seq)
    current_damage = compute_damage(seq_summary)

    if D < minimum:
        return "IMPOSSIBLE"
    if current_damage <= D:
        return 0
    else:
        return min_hacks(seq_summary, D)


# sequence = "SSCSSSSCSSSSSCS"
# seq_summary = summarize(sequence)
# print(save_the_universe(12, sequence))

#
# sequence = "SSCCSS"
# D = 5
# print(save_the_universe(D, sequence))

t = int(input())
for i in range(1, t + 1):
    D, P = [s for s in input().split(" ")]
    D = int(D)
    result = save_the_universe(D, P)
    print("Case #{}: {}".format(i, result))
