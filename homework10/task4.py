# Implement the counting sort algorithm to sort an array of non-negative integers.

def counting_sort(array):

    max_element = max(array)

    current_array = (max_element + 1) * [0]

    for i in array:
        current_array[i] += 1

    for i in range(1, max_element + 1):
        current_array[i] += current_array[i - 1]

    output_array = len(array) * [0]

    for i in range(len(array) -1, -1, -1):
        output_array[current_array[array[i]] - 1] = array[i]
        current_array[array[i]] -= 1

    return output_array

array = [4, 4, 5, 1, 4, 3, 3]
new = counting_sort(array)
print(new)


    