
class Heap:
    """Heap data structure to either be used as a minheap or maxheap"""

    def __init__(self):
        #Initialize heap array and size
        self.array = []
        self.size = 0

    #Add node to the max heap and swap nodes to maintain maxHeap properties
    def addNodeMax(self, val):
        if self.size == len(self.array):
            self.array.append(val)
        else:
            self.array[self.size] = val
        self.size += 1

        #Starting at the index inserted, continually swap with parent if conditions arent met
        current = self.size - 1
        parent = current // 2
        while self.array[parent] < self.array[current]:
            self.swapNodes(parent, current)
            current = parent
            parent = current // 2

    #Add node to the min heap and swap nodes to maintain minHeap properties
    def addNodeMin(self, val):
        if self.size == len(self.array):
            self.array.append(val)
        else:
            self.array[self.size] = val
        self.size += 1

        current = self.size - 1
        parent = current // 2
        while self.array[parent] > self.array[current]:
            self.swapNodes(parent, current)
            current = parent
            parent = current // 2


    #Swap two nodes (values) in the heap array
    def swapNodes(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]


    def heapifyMin(self, startIndex):
        """
        Alter the order of the heap array in order to maintain the minHeap property
        :param startIndex: The index to start the heapify process at. Usually 0 unless being called recursively
        :return: None, alters array of minheap instance
        """
        #Get locations of children nodes
        left_child = startIndex * 2 + 1
        right_child = startIndex * 2 + 2

        # If parent is greater than its children, swap with the child with smallest value
        if (left_child < self.size and self.array[left_child] < self.array[startIndex]) or (right_child < self.size and self.array[right_child] < self.array[startIndex]):

            if self.array[left_child] < self.array[right_child]:
                smallest_child = left_child
            else:
                smallest_child = right_child
            self.swapNodes(startIndex, smallest_child)

            #Recursively call heapify until entire heap is in correct ordering (satisfies minHeap conditions)
            self.heapifyMin(smallest_child)


    def heapifyMax(self, startIndex):
        """
        Alter the order of the heap array in order to maintain the maxHeap property
        :param startIndex: The index to start the heapify process at. Usually 0 unless being called recursively
        :return: None, alters array of maxheap instance
        """
        left_child = startIndex * 2
        right_child = startIndex * 2 + 1

        if (left_child < self.size and self.array[left_child] > self.array[startIndex]) or (right_child < self.size and self.array[right_child] > self.array[startIndex]):
            if self.array[left_child] > self.array[right_child]:
                largest_child = left_child
            else:
                largest_child = right_child
            self.swapNodes(startIndex, largest_child)
            self.heapifyMax(largest_child)


    def extractMin(self):
        #Get the smallest value
        root = self.array[0]

        #Place the last value into the root index and decrement the heap size
        self.array[0] = self.array[self.size-1]
        self.size -= 1

        #heapify to re-attain minheap properties
        self.heapifyMin(0)

        return root


    def extractMax(self):

        root = self.array[0]

        self.array[0] = self.array[self.size-1]
        self.size -= 1

        self.heapifyMax(0)

        return root


def medianManagement(values):
    """
    Continually calculates the median of a set of integers given one at a time.
    :param values: A list of all the integers to be added to the set
    :return: meds, A list of the medians for each iteration
    """

    #Instantiate a minheap and a maxheap
    minHeap = Heap()
    maxHeap = Heap()
    #Initialize the median as null
    median = None
    #Count iterations
    i = 1

    meds = []

    #Take each value one by one and calculate the median
    for val in values:
        #If this is the first number, set it to the median and continue to next number
        if median == None:
            median = val
            meds.append(median)
            print("Median at iteration {}: {}".format(i, median))
            i += 1
            continue
        #if the given value is less than the median, add it to the maxheap
        if val < median:
            maxHeap.addNodeMax(val)
        #If given value is greaer than or equal to median, add it to the minHeap
        else:
            minHeap.addNodeMin(val)

        #If either of the heaps is 2 larger than the other, shift and replace median
        #If maxheap is bigger
        if maxHeap.size > minHeap.size + 1:
            #push the median to the minheap
            minHeap.addNodeMin(median)
            #replace median with max value of maxheap
            median = maxHeap.extractMax()

        #if minheap is bigger
        elif minHeap.size > maxHeap.size + 1:

            #push the median to the maxheap
            maxHeap.addNodeMax(median)
            #replace median with min value of minheap
            median = minHeap.extractMin()

        #Print the median every iteration
        print("Median at iteration {}: {}".format(i, median))
        meds.append(median)
        i += 1

    return meds


#test
arr = [4,6,2,4,7,9,5]

medianManagement(arr)



