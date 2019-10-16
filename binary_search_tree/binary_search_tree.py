class BinarySearchTree:
    def __init__(self, value):
        # set the value at the current node
        self.value = value
        # add ref to left child node
        self.left = None
        # add ref to the right child node
        self.right = None
        # hold the tree nodes here for faster access later
        self.nodes = {}

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if the new nodes value is less than our current ones value
        if value < self.value:
            # if there is no left child,
            if self.left is None:
                # place a new node here
                node = BinarySearchTree(value)
                self.left = node
                # store the value and node
                self.nodes[node.value] = node
                return
            # otherwise if the right is empty and the value is greater than the node value
            elif self.left.right is None and value > self.left.value:
                node = BinarySearchTree(value)
                self.left.right = node
                # store the value and node
                self.nodes[node.value] = node
                return

            if value < self.left.value:
                self.left = self.left.left
                self.insert(value)
            else:
                self.left.right = self.left.right.right
                self.insert(value)

        else:
            if self.right is None:
                # place a new node here
                node = BinarySearchTree(value)
                self.right = node
                # store the value and node
                self.nodes[node.value] = node
                return
            # otherwise if the left is empty and the value is less than the node value
            elif self.right.left is None and value < self.right.value:
                node = BinarySearchTree(value)
                self.right.left = node
                # store the value and node
                self.nodes[node.value] = node
                return

            if value > self.right.value:
                self.right = self.right.right
                self.insert(value)
            else:
                if self.right.left:
                    self.right.left = self.right.left.left
                    self.insert(value)

    def contains(self, target):
        # if the target can be found in any of the root, left or right node
        if target == self.value or target == self.left.value or target == self.right.value:
            return True

        # BASE CASE
        elif self.left is None and self.right is None:
            return False

        # LEFT CASE
        if target < self.value:
            # if the is no left child,
            if self.left is None:
                return False
            # otherwise
            elif self.left.right is None:
                return False

            if value < self.left.value:
                self.left = self.left.left
                self.contains(value)

        else:
            # if the is no right child,
            if self.right is None:
                return False
            # otherwise
            elif self.right.left is None:
                return False

            if value > self.right.value:
                self.right = self.right.right
                self.contains(value)

    def get_max(self):
        # if there is no right node
        if self.right is None:
            return self.value

        # if the the is no right right value
        if self.right.right is None:
            return self.right.value

       # call the recursive function
        self.right = self.right.right
        self.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call the cb on the root
        cb(self.value)

        # call it on the nodes too
        [cb(key) for key in self.nodes.keys()]
            


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BinarySearchTree(5)


# bst.insert(2)
# bst.insert(3)
# # bst.insert(7)
# # bst.insert(6)
# print(bst.left.right.value)
# # print(bst.right.left.value)
