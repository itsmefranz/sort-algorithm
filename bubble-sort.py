def bubble_sort(array):
    n = len(array)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

array = [11, 64, 34, 25, 12, 6, 22, 36, 11, 90]