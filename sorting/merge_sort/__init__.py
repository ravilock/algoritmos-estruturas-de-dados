def merge_sort(array, start = None, end = None):
    if len(array) <= 1:
        return 
    if start == None:
        start = 0
    if end == None:
        end = len(array)
    if start >= end:
        return
    mid = (start + end) // 2
    if start >= mid:
        return
    merge_sort(array, start, mid)
    merge_sort(array, mid, end)
    combine(array, start, mid, end)

def combine(array, start, mid, end):
    if start >= mid:
        return
    aux = []
    a = start
    b = mid
    while a != mid and b != end:
        if array[a] <= array[b]:
            aux.append(array[a])
            a += 1
        else:
            aux.append(array[b])
            b += 1
    if a == mid:
        for i in range(b, end):
            aux.append(array[i])
    if b == end:
        for i in range(a, mid):
            aux.append(array[i])
    for value in aux:
        array[start] = value
        start += 1
