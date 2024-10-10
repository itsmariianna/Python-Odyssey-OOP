# Implement the Bubble Sort algorithm
# Ժամանակայնին բարդությունը վատագույն դեպքում O(n²)
# Ժամանակայնին բարդությունը միջին դեպքում O(n²)
# Ժամանակային բարդությունը լավագույն դեպքում O(n)
# Տարածքային բարդությունը O(1)

ls = [2, 6, 1, 9, 10, 4, 11]
size = len(ls)

for j in range(size - 1):

    flag = False

    for i in range(size - 1 - j):
        if ls[i] > ls[i + 1]:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
            flag = True

    if not flag:
        break

print(ls)
