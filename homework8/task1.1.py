# Implement the Bubble Sort algorithm (Recursive)

def recursive_bubble_sort(ls, n = None):
    if n is None:
        n = len(ls)

    elif n == 1:
        return ls

    flag = False
    for i in range(n - 1):
        if ls[i] > ls[i + 1]:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
            flag = True

    if not flag:
        return ls

    return recursive_bubble_sort(ls, n - 1)


my_list = [3, 5, 1, 2, 7, 18, 0, 6]
sorted_list = recursive_bubble_sort(my_list)
print(sorted_list)
