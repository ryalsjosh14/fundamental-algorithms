import unittest
from .DataStructures import RedBlackTree as rb


class SelectionTests(unittest.TestCase):


    """TODO: implement thorough tests"""

    def setUp(self):
        self.test_tree = rb.RedBlackTree()
        #test_tree.insert(6)
        #test_tree.insert(11)
        #test_tree.insert(8)

        #test_tree.delete(5)


    def test_insert_root(self):
        self.test_tree.insert(3)
        self.assertEqual(self.test_tree.root.key, 3, "Root key incorrect" )
        self.assertEqual(self.test_tree.root.left, None, "Root left child incorrect" )
        self.assertEqual(self.test_tree.root.right, None, "Root right child incorrect" )
        self.assertEqual(self.test_tree.root.color, 1, "Root not black" )

    def test_insert_black_parent(self):
        self.test_tree.insert(5)
        #self.assertEqual(self.test_tree.root.right.key, 5, "key incorrect")
        self.assertEqual(self.test_tree.root.left, None, "left child incorrect")
        #self.assertEqual(self.test_tree.root.right.right, None, "right child incorrect")
        #self.assertEqual(self.test_tree.root.right.parent.key, 3, "parent incorrect")
        #self.assertEqual(self.test_tree.root.right.color, 0, "color incorrect")


    def test_delete(self):
        pass




if __name__ == '__main__':
    unittest.main()