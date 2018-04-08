def check_sort(v_even, v_odd):
    merged_list = [v_even[i // 2] if i % 2 == 0 else v_odd[i // 2] for i in range(len(v_odd) + len(v_even))]

    for i in range(len(merged_list) - 1):
        if merged_list[i] > merged_list[i + 1]:
            return i
    return "OK"


def predict(v):
    v_even = sorted(v[0::2])
    v_odd = sorted(v[1::2])

    return check_sort(v_even, v_odd)


t = int(input())
for i in range(1, t + 1):
    N = int(input())
    V = [int(s) for s in input().split(" ")]
    result = predict(V)
    print("Case #{}: {}".format(i, result))
