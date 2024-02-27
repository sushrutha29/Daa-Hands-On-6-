import random

def partition(array, low, high):
    pivot_index = random.randint(low, high)
    pivot = array[pivot_index]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]

def quicksort_algorithm(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort_algorithm(array, low, pivot_index)
        quicksort_algorithm(array, pivot_index + 1, high)


array = [9, 5, 2, 12, 4, 7]
quicksort_algorithm(array, 0, len(array) - 1)
print("Sorted array using Random Pivot:", array)

#output: Sorted array using Random Pivot: [2, 4, 5, 7, 9, 12]
