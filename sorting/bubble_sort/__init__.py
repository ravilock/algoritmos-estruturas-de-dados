def bubble_sort(array):
    if len(array) <= 1:
        return
    for i in range(len(array)):
        swaps = 0
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] 
                swaps += 1
        if swaps == 0:
            break

def shaker_sort(array):
    if len(array) <= 1:
        return
    for i in range(len(array)):
        swaps = 0
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] 
                swaps += 1
        if swaps == 0:
            break
        for j in range(len(array)-1-i, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j] 
                swaps += 1
        if swaps == 0:
            break
