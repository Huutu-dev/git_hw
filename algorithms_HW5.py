
def selection_sort(arr):
    """ 1. Selection Sort
    Implement the selection sort algorithm that is sorting in descending order.
    """
    for i in range(len(arr)):
        k = i
        for j in range(i+1, len(arr)):
            if arr[k] < arr[j]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr


def bubble_sort(arr):
    """ 2. Bubble Sort
    Implement the bubble sort algorithm that is sorting in descending order.
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]

    return arr


def insertion_sort(arr):
    """ 3. Insertion Sort
    Implement the insertion sort algorithm that is sorting in descending order.
    """
    for i in range(1, len(arr)):
        pivot = arr[i]
        j = i
        while j > 0 and arr[j-1] < pivot:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = pivot
    return arr


def merge_sort(array):
    """ 4. Merge Sort
    Implement the merge sort algorithm that is sorting in descending order.
    """
    def merge_arrays(left: list, right: list) -> list:
        buff = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                buff.append(left[i])
                i += 1
                if i == len(left):
                    buff += right[j:]
                    # break
            else:
                buff.append(right[j])
                j += 1
                if j == len(right):
                    buff += left[i:]
                    # break
        return buff

    def do_recursive(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        return merge_arrays(do_recursive(arr[:mid]), do_recursive(arr[mid:]))

    return do_recursive(array)


import random
def run_test(fnc):
    sample = [23, 23, 9, 6, 18, 18, 25, 20, 10, 11]
    expect = sorted(sample, reverse=True)
    actual = fnc(sample[:])
    assert actual == expect, print(f"sample: {sample}, \nactual: {actual}, \nexpect: {expect}")

    N = 500
    sample = [random.randrange(4*N) for _ in range(N)]
    expect = sorted(sample, reverse=True)
    actual = fnc(sample[:])
    assert actual == expect, print(f"sample: {sample}, \nactual: {actual}, \nexpect: {expect}")


run_test(merge_sort)