def merge_sort(array):
    if len(array) > 1:
        mid = len(arr)//2
        L = array[:mid]
        R = array[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

array = [11, 16, 21, 4, 32, 51, 20, 45, 5, 1]
merge_sort(array)
print(array)