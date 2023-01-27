def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)


array = [10, 7, 8, 9, 1, 5]
n = len(array)

quick_sort(array, 0, n-1)

print ("Sorted array:", array)