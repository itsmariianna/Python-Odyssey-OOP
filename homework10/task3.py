# Write a program that sorts an array using insertion sort but skips sorting elements that are already in the correct position

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key

array = [2, 5, 6, 1, 9, 10, 3]
insertion_sort(array)
print(array)

