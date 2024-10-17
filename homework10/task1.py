# Implement insertion sort to sort an array of integers in ascending order.

def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


array = [2, 4, 1, 5, 6, 11, 9]
insertion_sort(array)
print(array)


