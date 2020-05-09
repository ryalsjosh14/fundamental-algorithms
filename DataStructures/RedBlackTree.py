
class RedBlackNode:
    """
    Creates a node object for a red-black tree. Color codes: 0:red, 1:black
    """

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

    def __str__(self):
        color = "Red" if self.color == 0 else "black"
        color = "double black" if self.color == 2 else color
        if self.parent != None:
            parent = self.parent.key
        else:
            parent = None
        return "{}, {}, parent: {}".format(self.key, color, parent)


class RedBlackTree:

    """TODO: Look for other methods to implement
    TODO: Add comments and test all methods (delete)"""

    def __init__(self):
        self.root = None
        self.size = 0


    def insert(self, key):
        #Create new node with specified key
        new_node = RedBlackNode(key)
        #Make new node red
        new_node.color = 0

        #If the tree is empty, set this node to the root and return
        if self.root == None:
            new_node.color = 1
            self.root = new_node
            return

        #Perform a regular BST search to find where to insert the new node
        curr_node = self.root

        #Continually search down the tree until a null pointer is found
        while True:

            #If new node is less than current node, search left subtree
            if key < curr_node.key:
                if curr_node.left == None:
                    curr_node.left = new_node
                    break
                else:
                    curr_node = curr_node.left
            #If new node is greater than or equal to current node, search right subtree
            else:
                if curr_node.right == None:
                    curr_node.right = new_node
                    break
                else:
                    curr_node = curr_node.right

        #set the parent of the new node as the last node searched before insertion
        new_node.parent = curr_node

        #while the current node's color is red, perform color swaps or rotations to keep RB tree property
        while curr_node.color == 0:

            #Get grandparent
            w = curr_node.parent
            #Initialize uncle as null
            z = None
            #Find uncle if it exists
            if w.left == curr_node and w.right != None:
                z = w.right

            elif w.left != None:
                z = w.left

            #Case 1, parent node has another child (uncle) which is red
            if z != None and z.color == 0:
                #swap colors

                z.color = 1
                curr_node.color = 1
                w.color = 0

                new_node = w
                curr_node = w.parent if w.parent != None else w

            #Case 2, parent node either does not have another child or child is black
            elif z == None or z.color == 1:
                #if current node is a left child
                if curr_node.parent.left == curr_node:

                    #If the new node is a right child, perform left rotaion to make it a left child
                    if new_node == curr_node.right:
                        self.left_rotate(curr_node, new_node)
                        curr_node, new_node = new_node, curr_node

                    #set the current node to black and the grandparent node to red, then right rotate the two
                    curr_node.color = 1
                    w.color = 0
                    self.right_rotate(w, curr_node)

                #Current node is right child
                else:
                    #If the new node is a left child, perform right rotaion to make it a right child
                    if new_node == curr_node.left:
                        self.right_rotate(curr_node, new_node)
                        curr_node, new_node = new_node, curr_node

                    #set the current node to black and the grandparent node to red, then left rotate the two
                    curr_node.color = 1
                    w.color = 0
                    self.left_rotate(w, curr_node)

            #Ensure root color is still black
            self.root.color = 1

            #If a rotation was performed about the root, break
            if curr_node == self.root:
                break

        #Increment size of tree
        self.size += 1


    def delete(self, key):
        """
        Performs standard BST delete, then calls RB_delete to deal with coloring issues specific to RB trees
        :param key:
        :return:
        """

        # Find the node to be deleted by searching for the input key
        node_to_delete = self.BSTSearch(key)

        #Adjust tree until node to be deleted is in a valid position (1 child or no children)
        while True:

            #Easy case (node to delete has no children)
            if node_to_delete.left == None and node_to_delete.right == None:
                #Directly call RB_delete
                self.RB_delete(node_to_delete)
                break

            #hard case (node to delete has 2 children)
            elif node_to_delete.left and node_to_delete.right:

                #find predeccessor
                predecessor = self.maximum(node_to_delete.left)

                #Swap the node to delete with its predecessor
                node_to_delete.color, predecessor.color = predecessor.color, node_to_delete.color
                self.swap_node(node_to_delete, predecessor)

            #medium case (node to delete has only 1 child)
            else:
                #Find child node
                child = node_to_delete.left if node_to_delete.left != None else node_to_delete.right

                #Replace node to delete with child, then call RB_delete with child node
                child.parent = node_to_delete.parent
                self.RB_delete(node_to_delete, child)
                break




    def RB_delete(self, v, u=None):
        """
        Performs all re-coloring and rotations needed to remove the given node and maintain a valid RB tree
        :param v: The node to be deleted
        :param u: The child of the node to be deleted (default NONE)
        """

        #Simple case, node to remove or its child (if exists) is red
        if v.color == 0 or (u!= None and u.color == 0):
            #If node has a child, change its color to black
            if u != None:
                u.color = 1
            #Remove the node from the tree, process is done
            self.remove_node(v, u)
            return

        #both u and v are black

        #Remove the current node from the tree, but still use its properties for re-coloring and rotations
        self.remove_node(v)

        #If there is a child, replace node to remove with child
        if u != None:
            v = u

        # Make v double black
        v.color = 2

        #Continually perform rotations and/or re-coolorings until current node (v) is not labeled double black
        while v != None and v.color == 2:
            #Find sibling node
            s = v.parent.right if v == v.parent.left or v.parent.left == None else v.parent.left

            #Case a, s is black and at least one of its children is red
            if s != None and s.color == 1 and (s.left != None and s.left.color == 0 or s.right != None and s.right.color == 0):
                #Splits into 4 subcases

                #Left-left case: s is left child and s.left is red
                if s != None and s.parent.left == s and s.left != None and s.left.color == 0:
                    #Set left child color to black and right rotate
                    s.left.color = 1
                    self.right_rotate(s.parent, s)

                #Right-right case: Mirror case of above, s is right child and s.right is red
                elif s != None and s.parent.right == s and s.right != None and s.right.color == 0:
                    #Set right child color to black and left rotate
                    s.right.color = 1
                    self.left_rotate(s.parent, s)

                #Left-right case: s is left child and s.right is red
                elif s != None and s.parent.left == s and s.right != None and s.right.color == 0:

                    child = s.right
                    self.left_rotate(s, child)
                    s, child = child, s
                    s.color = 1
                    self.right_rotate(s.parent, s)

                #Right-left case: Mirror case of above, s is right child and s.left is red
                elif s != None and s.parent.right == s and s.left != None and s.left.color == 0:
                    child = s.left
                    self.right_rotate(s, child)
                    s, child = child, s
                    s.color = 1
                    self.left_rotate(s.parent, s)

                #Ensure that color of current node is re-set to black (from double-black), then break
                v.color = 1
                break

            #Case b, sibling is black but does not have a red child
            elif s != None and s.color == 1:
                #Re-color sibling as red
                s.color = 0

                #current node becomes black
                v.color = 1

                #If the parent was black, it becomes double black so recurse
                if s.parent.color == 1:
                    v = s.parent
                    v.color = 2

                #If the parent was red, just make it black
                else:
                    s.parent.color = 1

            #Case c: sibling is red
            else:
                parent = s.parent
                #if sibling is the right child, perform left rotation
                if s == s.parent.right:
                    #If sibling's right child is black, then the left child needs to be set to red before left rotation
                    if s.color == 0 and s.right != None and s.right.color == 1 and s.left != None:
                        s.left.color = 0

                    #Set sibling to black and perform rotation
                    s.color = 1
                    self.left_rotate(parent, s)
                    v = parent.left
                else:
                    #If sibling's left child is black, then the right child needs to be set to red before right rotation
                    if s.color == 0 and s.left != None and s.left.color == 1 and s.right != None:
                        s.right.color = 0

                    #Set sibling to black and perform rotation
                    s.color = 1
                    self.right_rotate(parent, s)
                    v = parent.right

            if v == self.root:
                v.color = 1
                break


    def maximum(self, node):
        """
        Find maximum node in subtree of given node
        """
        while node.right != None:
            node = node.right
        return node

    def swap_node(self, node, predecessor):
        """
        Swaps a node and its predeccesor in a tree. This does not change coloring,
        which should be changed outside this function
        :param node: Node to be swapped
        :param predecessor: predecessor of given node
        :return:
        """
        #If node is the root, set the root to be the predecessor
        if node == self.root:
            self.root = predecessor
        else:
            #If not, set the node parent child pointer to point to predeccessor
            if node.parent.right == node:
                node.parent.right = predecessor
            else:
                node.parent.left = predecessor

        #Set parent pointers for children of predecessor and node
        if node.right != None:
            node.right.parent = predecessor
        if predecessor.left != None:
            predecessor.left.parent = node


        #If the predeccessor is the left child of node, swap different properties to avoid double pointers
        if predecessor == node.left:

            #Swap parents
            predecessor.parent = node.parent
            node.parent = predecessor

            #swap child pointers
            node.left = predecessor.left
            predecessor.left = node
            predecessor.right = node.right
            node.right = None
            return

        #If predecessor is not direct child

        #Reser predeccessor parent child pointer
        if predecessor.parent.right == predecessor:
            predecessor.parent.right = node
        else:
            predecessor.parent.left = node

        #reset left child parent pointer
        if node.left != None:
            node.left.parent = predecessor


        #Swap values
        node.parent, predecessor.parent = predecessor.parent, node.parent
        node.left, predecessor.left = predecessor.left, node.left
        predecessor.right = node.right
        node.right = None


    def remove_node(self, node_to_delete, child=None):
        """
        Remove the node from the tree by removing all pointers which point to the node
        """
        if node_to_delete == self.root:
            self.root = None
        elif node_to_delete.parent.left == node_to_delete:
            node_to_delete.parent.left = child
        else:
            node_to_delete.parent.right = child



    def left_rotate(self, x, y):
        if self.root == x:
            self.root = y
            y.color = 1

        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
            #print(y)
            #print("In leftrotate: {}".format(x.parent.right))

        y.parent = x.parent
        x.parent = y
        x.right = y.left
        y.left = x

        if x.right != None:
            x.right.parent = x


    def right_rotate(self, x, y):
        if self.root == x:
            self.root = y
            y.color = 1

        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

        y.parent = x.parent
        x.parent = y
        x.left = y.right
        y.right = x

        if x.left != None:
            x.left.parent = x

    def BSTSearch(self, key):
        curr_node = self.root

        while curr_node != None:

            if key == curr_node.key:
                break

            if key < curr_node.key:
                curr_node = curr_node.left
            elif key > curr_node.key:
                curr_node = curr_node.right

        return curr_node

    def printTree(self):
        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            curr_node = queue.pop(0)
            print(curr_node)
            if curr_node != None and (not (curr_node.left == None and curr_node.right==None)):
                queue.append(curr_node.left)
                queue.append(curr_node.right)



if __name__ == '__main__':
    #tests
    test_tree = RedBlackTree()
    test_tree.insert(3)
    test_tree.insert(5)
    test_tree.insert(6)
    test_tree.insert(11)
    test_tree.insert(8)

    test_tree.delete(5)
    test_tree.delete(11)
    test_tree.delete(8)


    test_tree.printTree()

    #print(test_tree.BSTSearch(9))

