import timeit
import matplotlib.pyplot as plot1

def partition(array, low, high):
    pivot = array[low]
    i = low

    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[low], array[i] = array[i], array[low]
    return i

def quicksort_algorithm(array, low, high):
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(array, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

n = [5, 10, 50, 100, 250, 500, 750, 1000, 1500, 2000, 2500, 4000, 7000]
execution_times = []

for size in n:
    input_data = generate_worst_case_input(size)
    time_taken = timeit.timeit(lambda: quicksort(input_data, 0, size - 1), number=10)
    execution_times.append(time_taken)

plot1.plot(n, execution_times, linestyle='--', marker='o')
plot1.title('Worst Case Performance of QuickSort Using Non-Random Pivot')
plot1.xlabel('Size (n)') 
plot1.ylabel('Execution Time Taken in Seconds')
plot1.show()
