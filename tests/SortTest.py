import unittest
from .divide_and_counquer import sorting as s


class SortTests(unittest.TestCase):

    def setUp(self):
        self.arr1 = [] #Empty array
        self.arr2 = [1] #One-element array
        self.arr3 = [3,23,3,5,1,7,12,5] #Even-number elements array with repeats
        self.arr4 = [4,6,2,4,7,9,5] #odd number elements array with repeats

    def test_bubble_sort(self):
        self.assertEqual(s.bubbleSort(self.arr1), [], 'Bubble sort with empty array failed')
        self.assertEqual(s.bubbleSort(self.arr2), [1], 'Bubble sort with array length 1 failed')
        self.assertEqual(s.bubbleSort(self.arr3), sorted(self.arr3))
        self.assertEqual(s.bubbleSort(self.arr4), sorted(self.arr4))

    def test_insertion_sort(self):
        self.assertEqual(s.insertionSort(self.arr1), [], 'insertion sort with empty array failed')
        self.assertEqual(s.insertionSort(self.arr2), [1], 'insertion sort with array length 1 failed')
        self.assertEqual(s.insertionSort(self.arr3), sorted(self.arr3))
        self.assertEqual(s.insertionSort(self.arr4), sorted(self.arr4))

    def test_selection_sort(self):
        self.assertEqual(s.selectionSort(self.arr1), [], 'selection sort with empty array failed')
        self.assertEqual(s.selectionSort(self.arr2), [1], 'selection sort with array length 1 failed')
        self.assertEqual(s.selectionSort(self.arr3), sorted(self.arr3))
        self.assertEqual(s.selectionSort(self.arr4), sorted(self.arr4))

    def test_merge_sort(self):
        self.assertEqual(s.mergeSort(self.arr1), [], 'merge sort with empty array failed')
        self.assertEqual(s.mergeSort(self.arr2), [1], 'merge sort with array length 1 failed')
        self.assertEqual(s.mergeSort(self.arr3), sorted(self.arr3))
        self.assertEqual(s.mergeSort(self.arr4), sorted(self.arr4))

    def test_quick_sort(self):
        self.assertEqual(s.quickSort(self.arr1, 0, 0), [], 'quick sort with empty array failed')
        self.assertEqual(s.quickSort(self.arr2, 0, 0), [1], 'quick sort with array length 1 failed')
        self.assertEqual(s.quickSort(self.arr3, 0, len(self.arr3)-1), sorted(self.arr3))
        self.assertEqual(s.quickSort(self.arr4, 0, len(self.arr4)-1), sorted(self.arr4))


if __name__ == '__main__':
    unittest.main()
