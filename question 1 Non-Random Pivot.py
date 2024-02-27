import random

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort_algorithm(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort_algorithm(array, low, pivot_index - 1)
        quicksort_algorithm(array, pivot_index + 1, high)

array = [9, 5, 2, 12, 4, 7]
quicksort_algorithm(array, 0, len(array) - 1)
print("Sorted array using Non-Random Pivot:", array)

#output: Sorted array using Non-Random Pivot: [2, 4, 5, 7, 9, 12]
