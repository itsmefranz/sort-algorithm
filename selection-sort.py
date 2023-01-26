def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j

        array[i], array[min] = array[min], array[i]
        print(array)

array = [21, 3, 56, 9, 6, 41, 22, 18, 23, 71]

selection_sort(array)
print("Sorted array:", array)