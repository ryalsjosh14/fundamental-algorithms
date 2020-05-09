import random
from .sorting import mergeSort
from .DivideAndConquer import mergeSortPairs


def randomizedSelection(arr, i):
    """
    Returns the ith order statistic from a given array using random pivots
    :param arr: Input array
    :param i: The ith order statistic to be selected
    :return: The ith-order statistic of the given input array (arr).
    """
    n = len(arr)

    #Base case
    if n == 1:
        return arr[0]

    #Use random pivot value
    pivot = random.randint(0, n-1)
    #partition arr around pivot
    j = partition(arr, pivot, n)

    #If correct location of the pivot is the ith-1 location, return the value at that location
    if j == (i-1):
        return arr[j]
    #If current location of pivot is less than the location of the ith statistic, recursively solve on right side of array
    elif j < (i-1):
        return randomizedSelection(arr[j+1:], i-(j+1))
    #If current location of pivot is more than the location of the ith statistic, recursively solve on left side of array
    elif j > (i-1):
        return randomizedSelection(arr[:j+1], i)


def detSelect(arr, i):
    """
    Returns the ith order statistic from a given array using deterministic pivots (median of medians)
    :param arr: Input array
    :param i: The ith order statistic to be selected
    :return: The ith-order statistic of the given input array (arr).
    """
    #get length of input array
    n = len(arr)

    #base case
    if n <= 5:
        new_arr = mergeSort(arr)
        return new_arr[i-1]

    #Get pivot location with deterministic approach
    pivot = choosePivot(list(enumerate(arr)), n)
    pivot = pivot[0]

    # partition arr around pivot
    j = partition(arr, pivot, n)

    # If correct location of the pivot is the ith-1 location, return the value at that location
    if j == (i - 1):
        return arr[j]

    # If current location of pivot is less than the location of the ith statistic,
    # recursively solve on right side of array
    elif j < (i - 1):
        return detSelect(arr[j+1:], i - (j + 1))

    # If current location of pivot is more than the location of the ith statistic,
    # recursively solve on left side of array
    elif j > (i - 1):
        return detSelect(arr[:j + 1], i)


def choosePivot(A, n):
    """
    Utility function for deterministic selection. Selects the pivot location using median of medians
    :param A: Array of which to find the pivot
    :param n: The length of the input array
    :return: The pivot location and its value
    """
    #Initialize array of medians
    C = []

    #Split input array into groups of 5
    for i in range(0, n, 5):
        #If in the last group in the array (with length not equal to 5), ignore the last few numbers
        if i+5 > n:
            continue
        else:
            end = i + 5

        #Sort the group of 5 using merge sort (O(nlogn)
        new_sort = mergeSortPairs(A[i:end], index=1)
        #FInd the median of this group and append to array of medians
        med = new_sort[2]
        C.append(med)
    # if there is only one median left, return this median
    if len(C) == 1:
        return C[0]
    #Recursively compute the median of the medians
    return choosePivot(C, len(C))


def partition(A, pivot, n):
    """
    Utility function which partitions array around pivot point
    :param A: Array to be partitioned
    :param pivot: Location to pivot array around
    :param n: Length of array
    :return: The correct (sorted) index of the pivot location
    """
    #Swap the pivot value with the first value in array
    A[0], A[pivot] = A[pivot], A[0]
    #Start the iteration with the second value in array
    newPivotIndex = 1
    for index in range(1, n):
        if A[index] < A[0]:  # check if current val is less than pivot value
            #Move current index value into unpartitioned part of array
            A[index], A[newPivotIndex] = A[newPivotIndex], A[index]
            #Increment new Pivot index
            newPivotIndex = newPivotIndex + 1



    #Move pivot to position between <value and >values (index just before newPivotIndex)
    A[0], A[newPivotIndex-1] = A[newPivotIndex-1], A[0]

    #Return new position of pivot value
    return newPivotIndex - 1
