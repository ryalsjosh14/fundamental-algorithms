import unittest
from .divide_and_counquer import selecting as sel


class SelectionTests(unittest.TestCase):

    def setUp(self):
        self.arr1 = [1] #One-element array
        self.arr2 = [3,23,3,5,1,7,12,5] #Even-number elements array with repeats
        self.arr3 = [4,6,2,4,7,9,5] #odd number elements array with repeats
        self.arr4 = [1,5,3,7,6,9,4,6,9,12,3,54,3,2,22,43,13,16,53,65,78,76,9]

    def test_random_select(self):
        self.assertEqual(sel.randomizedSelection(self.arr1, 1), 1)
        self.assertEqual(sel.randomizedSelection(self.arr2, 5), 5)
        self.assertEqual(sel.randomizedSelection(self.arr2, 6), 7)
        self.assertEqual(sel.randomizedSelection(self.arr3, 1), 2)
        self.assertEqual(sel.randomizedSelection(self.arr3, 1), 2)
        self.assertEqual(sel.randomizedSelection(self.arr4, 10), sorted(self.arr4)[9])

    def test_deterministic_select(self):
        self.assertEqual(sel.detSelect(self.arr1, 1), 1)
        self.assertEqual(sel.detSelect(self.arr2, 5), 5)
        self.assertEqual(sel.detSelect(self.arr2, 6), 7)
        self.assertEqual(sel.detSelect(self.arr3, 1), 2)
        self.assertEqual(sel.detSelect(self.arr3, 1), 2)
        self.assertEqual(sel.detSelect(self.arr4, 10), sorted(self.arr4)[9])



if __name__ == '__main__':
    unittest.main()