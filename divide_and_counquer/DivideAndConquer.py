import numpy as np
import math

def countInversions(arr):
    """
    Counts the number of inversions present in the given array. An inversion is defined as an array element which is
    less than an element which comes before it (out of sorted order). Therefore, sorted arrays have 0 inversions, while
    an array sorted in descending order has n + (n-1) + ... + 1 inversions
    :param arr: Input list
    :return: tuple of the sorted array and the number of inversions present in the original array
    """

    # Get length of array
    arr_length = len(arr)

    # Base case, if length is 1, return the entire array
    if arr_length <= 1:
        return arr, 0

    # Split array into left and right side
    left_arr = arr[0:(arr_length // 2)]
    right_arr = arr[(len(arr) // 2):len(arr)]

    # Recursively sort the left and right arrays
    leftSide, left_inversions = countInversions(left_arr)
    rightSide, right_inversions = countInversions(right_arr)

    # Merge
    # Initialize a pointer for each array
    first_idx = 0
    second_idx = 0

    # Initialize solution array as the sum of left and right inversions
    sol = left_inversions + right_inversions
    sortedArr = []

    # Track if all of the indeces of second array have been visited
    is_second_done = False

    for i in range(0, arr_length):

        # If the next value in first array is less than next in second, or if second is "empty",
        # append next val in first to solution
        if is_second_done or (first_idx < len(leftSide) and leftSide[first_idx] <= rightSide[second_idx]):
            sortedArr.append(leftSide[first_idx])
            first_idx += 1

        # If not append next value in second array
        else:
            # If number is pulled from right, it is less than all the remaining numbers in left
            sol += len(leftSide) - first_idx
            sortedArr.append(rightSide[second_idx])

            if second_idx == len(rightSide) - 1:
                is_second_done=True
            else:
                second_idx += 1

    # Return solution array
    return sortedArr, sol

#Utility function for strassens
def matrixSplit(mat):
    #Get dimensions of input matrix
    rows, cols = np.shape(mat)

    #Get mid point of matrix horizontally and vertically
    midVert = cols//2
    midHoriz = rows//2

    #Return 4 quadrants of the matrix
    return mat[:midHoriz, :midVert], mat[:midHoriz, midVert:], mat[midHoriz:, :midVert], mat[midHoriz:, midVert:]

def strassens(x,y):
    """
    Multiplies two matrices using Strassen's formula. This achieves a running time < O(n^3), which is the running time
    for the "brute force" matrix multiplication algorithm
    :param x: matrix A
    :param y: matrix B
    :return: Matrix C, the product of x and y
    """

    x = np.asarray(x)
    y = np.asarray(y)

    #Base case
    if len(x) == 1:
        return x*y

    a,b,c,d = matrixSplit(x)
    e,f,g,h = matrixSplit(y)

    #Recursively compute the seven Strassen products
    p1 = strassens(a, (f-h))
    p2 = strassens(a+b, h)
    p3 = strassens(c+d, e)
    p4 = strassens(d, g-e)
    p5 = strassens(a+d, e+h)
    p6 = strassens(b-d, g+h)
    p7 = strassens(a-c, e+f)

    #Calculate the four quadrants by calculating the Strassen sums
    q1 = p5+p4-p2+p6
    q2 = p1+p2
    q3 = p3+p4
    q4 = p1+p5-p3-p7

    #Create solution rows with hstack
    row1 = np.hstack((q1,q2))
    row2 = np.hstack((q3,q4))

    #Vertically stack solution rows and return final product matrix
    return np.vstack((row1, row2))


def closestPair(points):
    """
    Finds the two points on a grid with smallest distance between them.
    :param points: A list of coordinate pairs
    :return: A list containing the two closest coordinate points
    """
    #Input: Array of coordinate pairs

    #Sort points by x coordinate(Px) and y coordinate(Py)
    Px = mergeSortPairs(points, 0)
    Py = mergeSortPairs(points, 1)

    #Base Case: If there are only 2 points, return those points
    if len(points) < 3:
        return points
    #Find the middle index
    midPoint = len(points) // 2

    # Break points into left half and right half
    Qx = Px[:midPoint]
    #Qy = Py[midPoint:]
    Rx = Py[:midPoint]
    #Ry = Py[midPoint:]

    #Recursively get closest pair in left half and right half, as well as their respective distance
    [p1,q1] = closestPair(Qx)
    dist1 = calcDist(p1,q1)
    [p2,q2] = closestPair(Rx)
    dist2 = calcDist(p2,q2)

    #Set lambda to the small distance found without split pairs
    lam = min(dist1, dist2)

    #Find the closest split pair and its distance
    [p3, q3], dist3 = closestSplitPair(Px, Py, lam)

    #Get the smallest distance of the three, and return its corresponding pair
    bestDist = min(dist1, dist2, dist3)
    if bestDist == dist1:
        sol = [p1, q1]
    elif bestDist == dist2:
        sol = [p2, q2]
    else:
        sol = [p3, q3]

    return sol




def closestSplitPair(Px, Py, lam):
    midpoint = len(Px)//2
    Xbar = Px[midpoint][0]

    Sy = []
    for point in Py:
        if point[0] > (Xbar-lam) and point[0] < (Xbar+lam):
            Sy.append(point)

    bestDist = lam
    bestPoint = None

    for i in range(len(Sy)-1):
        for j in range(min(7,len(Sy)-i)):
            p, q = Sy[i], Sy[i+1]
            dist = calcDist(p,q)
            if dist < bestDist:
                bestDist = dist
                bestPoint = [p, q]

    return bestPoint, bestDist




def calcDist(p,q):
    diffX = p[0] - q[0]
    diffY = p[1] - q[1]

    return math.sqrt(diffX**2 + diffY**2)

#Adjusted merge sort which sorts ordered pairs based on given index (x or y, x = 0, y = 1)
def mergeSortPairs(arr, index):
    # Get length of array
    arr_length = len(arr)
    # Base case, if length is 1, return the entire array
    if arr_length == 1:
        return arr

    # Split array into left and right side
    left_arr = arr[0:(arr_length // 2)]
    right_arr = arr[len(arr) // 2:len(arr)]

    # Recursively sort the left and right arrays
    first_sol = mergeSortPairs(left_arr, index)
    second_sol = mergeSortPairs(right_arr,index)

    # Merge
    # Initialize a pointer for each array
    first_idx = 0
    second_idx = 0
    # Initialize solution array as empty
    sol = []

    # Track if all of the indeces of second array have been visited
    is_second_done = False

    for i in range(0, arr_length):

        # If the next value in first array is less than next in second, or if second is "empty",
        # append next val in first to solution
        if is_second_done or (first_idx < len(first_sol) and first_sol[first_idx][index] < second_sol[second_idx][index]):
            sol.append(first_sol[first_idx])
            first_idx += 1
        # If not append next value in second array
        else:
            sol.append(second_sol[second_idx])
            if second_idx == len(second_sol) - 1:
                is_second_done = True
            else:
                second_idx += 1
    # Return solution array
    return sol


arr = [[3, 5], [2, 7], [7, 6], [8, 4], [15, 3], [32, 3], [1, 1], [14, 14]]
arr2 = [[23, 5], [4, 7]]
#arr = [5,5,5,5,5]
#(sortedArr, inversionCount) = countInversions(arr);
#print(sortedArr)
closest= closestPair(arr)
print(closest)