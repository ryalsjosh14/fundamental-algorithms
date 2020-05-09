import random
def bubbleSort(arr):
    didSwap = True
    while didSwap:
        didSwap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                didSwap = True
    return arr


def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr


def selectionSort(arr):
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

def mergeSort(arr):
    #Get length of array
    arr_length = len(arr)

    #Base case, if length is 1 or 0, return the entire array
    if arr_length < 2:
        return arr

    #Split array into left and right side
    left_arr = arr[0:(arr_length//2)]
    right_arr = arr[len(arr)//2:len(arr)]

    #Recursively sort the left and right arrays
    first_sol = mergeSort(left_arr)
    second_sol = mergeSort(right_arr)

    #Merge
    #Initialize a pointer for each array
    first_idx = 0
    second_idx = 0
    #Initialize solution array as empty
    sol = []
    #Track if all of the indeces of second array have been visited
    is_second_done = False

    for i in range(0,arr_length):

        #If the next value in first array is less than next in second, or if second is "empty",
        # append next val in first to solution
        if is_second_done or (first_idx < len(first_sol) and first_sol[first_idx] < second_sol[second_idx]):
            sol.append(first_sol[first_idx])
            first_idx += 1

        #If not append next value in second array
        else:
            sol.append(second_sol[second_idx])
            if second_idx == len(second_sol)-1:
                is_second_done = True
            else:
                second_idx += 1

    #Return solution array
    return sol


from random import randint


def quickSort(A, start, end):
    """

    :param A: Input array to be sorted in ascending order
    :param start: The start index of the array, initially zero, changes for recursive calls
    :param end: The last index to be sorted, initially the length of the array, changes for recursive calls
    :return: None, just mutates given array
    """

    #If there is still more of the array remaining to sort,repeat process
    if start < end:
        #partition the array with given start and end indices
        p = partition(A, start, end)

        #After aray has been partitiioned, execute quicksort with the array left of pivot and array right of pivot
        quickSort(A, start, p - 1)
        quickSort(A, p + 1, end)

    return A


def partition(A, start, end):
    #Randomly select pivot location with randint between start and end indices
    pivot = randint(start, end)

    #Swap the pivot value with the first value in array
    A[start], A[pivot] = A[pivot], A[start]
    #Start the iteration with the second value in array
    newPivotIndex = start + 1
    for index in range(start+1, end+1):
        if A[index] < A[start]:  # check if current val is less than pivot value
            #Move current index value into unpartitioned part of array
            A[index], A[newPivotIndex] = A[newPivotIndex], A[index]
            #Increment new Pivot index
            newPivotIndex = newPivotIndex + 1



    #Move pivot to position between <value and >values (index just before newPivotIndex)
    A[start], A[newPivotIndex-1] = A[newPivotIndex-1], A[start]

    #Return new position of pivot value
    return newPivotIndex - 1


'''
#tests
arr = [1,5,3,4,7,2,11,3,2,1]
arr2 = [1,5,3,4,7,2,11,3,2,1]
arr3 = [10,7,8,9,1,5]
arr4 = [72,56,13,43,25,84,32,1,5,45,87,69,96,45,36,67,56]
print("insert sort: {}".format(selectionSort(arr)))
#print("insertion sort: {}".format(insertionSort(arr2)))
#print("selection sort: {}".format(selectionSort(arr3)))
#print("Merge sort: {}".format(mergeSort(arr4)))
result = quickSort([3,23,3,5,1,7,12,5], 0, len(arr3)-1)
print("Quick sort: {}".format(result))
'''



