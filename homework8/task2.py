# Implement the Selection Sort algorithm.
# Ժամանակայնին բարդությունը վատագույն դեպքում O(n²)
# Ժամանակայնին բարդությունը միջին դեպքում O(n²)
# Ժամանակային բարդությունը լավագույն դեպքում O(n²)
# Տարածքային բարդությունը O(1)

arr = [2, 8, 5, 3, 9, 4, 1]
size = len(arr)

for i in range(size):
    min_index = i
    for j in range(i + 1, size):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)