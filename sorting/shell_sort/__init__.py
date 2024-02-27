SHRINK_FACTOR = 2.3

def shell_sort(array, k = None):
    if len(array) <= 1:
        return
    if k == None:
        k = round(len(array) / SHRINK_FACTOR)
    print(k)
    for i in range(1, len(array), k):
        sorted_boundary = i
        insertion_index = 0
        found = False
        for j in range(sorted_boundary - 1, insertion_index - 1, -k):
                if array[i] < array[j]:
                    insertion_index = j
                    found = True
        if not found:
            continue
        for j in range(sorted_boundary, insertion_index, -k):
            array[j], array[j - 1] = array[j - 1], array[j]
    if k == 1:
        return
    shell_sort(array, round(k / SHRINK_FACTOR))


def insertion_sort(array):
    if len(array) <= 1:
        return
    for i in range(1, len(array)):
        sorted_boundary = i
        insertion_index = 0
        found = False
        for j in range(sorted_boundary - 1, insertion_index - 1, -1):
            if array[i] < array[j]:
                insertion_index = j
                found = True
        if not found:
            continue
        for j in range(sorted_boundary, insertion_index, -1):
            array[j], array[j - 1] = array[j - 1], array[j]
