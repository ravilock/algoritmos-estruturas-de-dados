def quick_sort(array, start = None, end = None):
    if len(array) <= 1:
        return
    if start == None:
        start = 0
    if end == None:
        end = len(array) - 1
    if start > end:
        return
    pivotIndex = partition(array, start, end)
    quick_sort(array, start, pivotIndex - 1)
    quick_sort(array, pivotIndex + 1, end)

def partition(array, start, end):
    pivot = array[start]
    a = start + 1
    b = end
    while True:
        if a > b:
            break
        if array[a] < pivot:
            a += 1
        elif array[b] > pivot:
            b -= 1
        else:
            array[a], array[b] = array[b], array[a]
    array[start], array[a-1] = array[a-1], array[start]
    return a - 1
