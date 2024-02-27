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

def binary_insertion_sort(array):
    if len(array) <= 1:
        return
    for i in range(1, len(array)):
        sorted_boundary = i
        insertion_index = 0
        bottom_boundary = 0
        top_boundary = sorted_boundary
        found = False
        print()
        print(f"before: {array}, sorted_boundary={sorted_boundary}")
        while not found:
            j = (bottom_boundary + top_boundary) // 2
            print(f"j={j},bottom_boundary={bottom_boundary},top_boundary={top_boundary}")

# before: [0j, 9, 7*, 1, 6, 8, 2, 4, 3, 5], sorted_boundary=2
# j=1,bottom_boundary=0,top_boundary=2
# j=0,bottom_boundary=0,top_boundary=1

            if j == bottom_boundary:
                if array[sorted_boundary] < array[j]:
                    found = True
                    insertion_index = j
                break

            if array[j] > array[sorted_boundary]:
                top_boundary = j
                continue
            bottom_boundary = j
        if not found:
            continue
        for j in range(sorted_boundary, insertion_index, -1):
            array[j], array[j - 1] = array[j - 1], array[j]
        print(f"after:  {array}")
