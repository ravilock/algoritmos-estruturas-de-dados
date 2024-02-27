def selection_sort(array):
    if len(array) <= 1:
        return
    for i in range(len(array)):
        minBoundary = i
        minIndex = minBoundary
        for j in range(minBoundary, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        if array[minIndex] < array[minBoundary]:
            array[minBoundary], array[minIndex] = array[minIndex], array[minBoundary]

def double_selection_sort(array):
    if len(array) <= 1:
        return
    for i in range(len(array)):
        minBoundary = i
        maxBoundary = len(array) - 1 - i
        if maxBoundary <= minBoundary:
            return
        minIndex = minBoundary
        maxIndex = maxBoundary
        for j in range(minBoundary, maxBoundary + 1):
            if array[j] < array[minIndex]:
                minIndex = j
            if array[j] > array[maxIndex]:
                maxIndex = j
        if maxIndex == minBoundary:
            maxIndex = minIndex
        if array[minIndex] < array[minBoundary]:
            array[minBoundary], array[minIndex] = array[minIndex], array[minBoundary]
        if array[maxIndex] > array[maxBoundary]:
            array[maxBoundary], array[maxIndex] = array[maxIndex], array[maxBoundary]
