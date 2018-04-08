def trouble_sort(L):
    done = False
    while not done:
        done = True
        for i in range(len(L) - 2):
            if L[i] > L[i + 2]:
                done = False
                L[i], L[i + 2] = L[i + 2], L[i]
    return L


def check_sort(v):
    well_sorted = True
    trouble_index = 0

    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            well_sorted = False
            trouble_index = i
    if well_sorted:
        return "OK"
    else:
        return trouble_index

# v = [1, 2, 3, 0, 5]
# v = [1,3, 2]

predict(v)

# for i in range(len(v_even) - 1) :
#     if v_odd[i] < v_even[i]:
#         return 2*i
#     if v_even[i+1] < v_odd[i]:
#         return 2*i + 1