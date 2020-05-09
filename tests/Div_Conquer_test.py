import unittest
from .divide_and_counquer import DivideAndConquer as div


class SelectionTests(unittest.TestCase):

    def test_inversion_count(self):
        arr1 = [1,3,5,2,4,6]
        arr2 = [3,5,6,8,9,12,13]
        arr3 = []
        arr4 = [1]
        arr5 = [13,12,9,8,6,5,3]

        self.assertEqual(div.countInversions(arr1), (sorted(arr1), 3), "unsorted array")
        self.assertEqual(div.countInversions(arr2), (sorted(arr2), 0), "sorted array")
        self.assertEqual(div.countInversions(arr3), (sorted(arr3), 0), "empty array")
        self.assertEqual(div.countInversions(arr4), (sorted(arr4), 0), "array length 1")
        self.assertEqual(div.countInversions(arr5), (sorted(arr5), 21), "backwards-sorted array")


    def test_strassens(self):
        pass

    def test_closest_points(self):
        #points1 = [[3, 5], [2, 7], [7, 6], [8, 4], [15, 3], [32, 3], [1, 1], [14, 14]]
        points2 = [[1,2], [65,63]]
        sol2 = div.closestPair(points2)
        self.assertTrue(sol2 == [[1,2],[65,63]] or sol2 == [[65, 63], [1,2]] )

        pass


if __name__ == '__main__':
    unittest.main()