from tree_node import TreeNode


class BinarySearchTree:
    def __init__(self, value):
        # set the value at the current node
        self.value = value
        # add ref to left child node
        self.left = None
        # add ref to the right child node
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if the new nodes value is less than our current ones value
        if value < self.value:
            # if the is no left child,
            if not self.left:
                # place a new node here
                self.left = BinarySearchTree(value)
                return
            # otherwise
            elif not self.left.right and self.left.value < value:
                self.left.right = BinarySearchTree(value)
                return

            if value < self.left.value:
                self.left = self.left.left
                self.insert(value)
            # else:
            #     self.left.right = self.left.right
            #     self.insert(value)

                # repeat process for left
        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current parent value
            # if there is no right child here,
                # place a new one
            # otherwise
                # repeat process right
        else:
            if not self.right:
                # place a new node here
                self.right = BinarySearchTree(value)
                return
            # otherwise
            elif not self.right.left and self.right.value > value:
                self.right.left = BinarySearchTree(value)
                return

            if value > self.right.value:
                self.right = self.right.right
                self.insert(value)
            # else:
            #     self.right.left = self.right.left
            #     self.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value or target == self.left.value or target == self.right.value:
            return True

        # BASE CASE
        elif self.left and not self.right:
            return False

        # LEFT CASE
        if target < self.value:
            # if the is no left child,
            if not self.left:
                return False
            # otherwise
            elif not self.left.right:
                return False

            if value < self.left.value:
                self.left = self.left.left
                self.contains(value)
            # else:
            #     # self.left.right = self.left.right
            #     # self.contains(value)
            #     pass

        else:
            # if the is no left child,
            if not self.right:
                return False
            # otherwise
            elif not self.right.left:
                return False

            if value > self.right.value:
                self.right = self.right.right
                self.contains(value)
            # else:
            #     # self.right.left = self.right.left
            #     # self.contains(value)
            #     pass

    # Return the maximum value found in the tree

    def get_max(self):
        # BASE CASE
        # if empty tree
        if self.right is None:
            return self.value
            # return none

        # RECURSIVE
        # if the the is no right value
        if self.right.right is None:
            return self.right.value

            # return the root value
        # return the get max of the the right node
        self.right = self.right.right
        self.get_max()

        # ITTERATIVE
        # set a max value variable to keep track of max value
        # get a ref to current node
        # check if we are at a valid tree node
        # if our current value is greater than the max value
        # update the max value
        # move on to the next right node in the tree
        # setting the current node to the current nodes right
        # return our max value
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        # base case

        # left case

        # right case

        # if target == self.value or target == self.left.value or target == self.right.value:
        #     return True

        # BASE CASE
        if self.left is None and self.right is None:
            return

        if self.left:
            cb(self.left.value)

            # if self.left:
            if self.left.left:
                cb(self.left.left.value)
                self.left = self.left.left
            if self.left.right:
                cb(self.left.right.value)
                self.left.right = self.left.right.right


        if self.right:
            cb(self.right.value)

            # if self.right:
            if self.right.right:
                cb(self.right.right.value)
                self.right = self.right.right
            if self.right.left:
                cb(self.right.left.value)
                self.right.left = self.right.left.left

        

        # LEFT CASE
        # if target < self.value:
        #     # if the is no left child,
        #     if not self.left:
        #         return False
        #     # otherwise
        #     elif not self.left.right:
        #         return False

        #     if value < self.left.value:
        #         self.left = self.left.left
        #         self.contains(value)
        #     # else:
        #     #     # self.left.right = self.left.right
        #     #     # self.contains(value)
        #     #     pass

        # else:
        #     # if the is no left child,
        #     if not self.right:
        #         return False
        #     # otherwise
        #     elif not self.right.left:
        #         return False

        #     if value > self.right.value:
        #         self.right = self.right.right
        #         self.contains(value)
        #     # else:
        #     #     # self.right.left = self.right.left
        #     #     # self.contains(value)
        #     #     pass

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
