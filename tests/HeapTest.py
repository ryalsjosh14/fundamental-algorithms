import unittest
from .DataStructures import heapOps as h


class SelectionTests(unittest.TestCase):

    def setUp(self):
        self.arr1 = [1] #One-element array
        self.arr2 = [3,23,3,5,1,7,12,5] #Even-number elements array with repeats
        self.arr3 = [4,6,2,4,7,9,5] #odd number elements array with repeats
        self.arr4 = [1,5,3,7,6,9,4,6,9,12,3,54,3,2,22]

    def test_median_manager(self):
        self.assertEqual(h.medianManagement(self.arr1), [1])
        self.assertEqual(h.medianManagement(self.arr2), [3,3,3,3,3,3,5,5])
        self.assertEqual(h.medianManagement(self.arr3), [4,4,4,4,4,4,5])
        self.assertEqual(h.medianManagement(self.arr4), [1,1,3,3,5,5,5,5,6,6,6,6,6,6,6])


if __name__ == '__main__':
    unittest.main()