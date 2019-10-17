from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    """Implementation of the Binary Search Tree data structure
    """

    def __init__(self, value):
        # set the value at the current node
        self.value = value
        # add ref to left child node
        self.left = None
        # add ref to the right child node
        self.right = None
        self.stack = Stack()

    def insert(self, value):
        """Inserts the value at the correct position

        Arguments:
            value {int} -- the value to be inserted into the tree
        """
        # if the value is less than the self.vale
        if value < self.value:
            # if there is no left node insert a new node here
            if self.left is None:
                self.left = BinarySearchTree(value)
            # otherwise call the insert method on the left node binary search tree instance
            else:
                self.left.insert(value)
        # otherwise
        else:
             # if there is no right node insert a new node here
            if self.right is None:
                self.right = BinarySearchTree(value)
            # otherwise call the insert method on the right node binary search tree instance
            else:
                self.right.insert(value)

    def contains(self, target):
        """Checks if a value is in a tree

        Arguments:
            target {int} -- value to be checked

        Returns:
            bool -- True if value is found and False otherwise
        """
        # if self.value is the target return True
        if target == self.value:
            return True

        # if target is less than self.target
        if target < self.value:
            # if there is no node to the left, then the target is not in the tree
            if self.left is None:
                return False
            # otherwise recursively call the contains method on the binary search tree instance of the left node
            else:
                return self.left.contains(target)
        # otherwise
        else:
            # if there is no node to the right, then the target is not in the tree
            if self.right is None:
                return False
            # otherwise recursively call the contains method on the binary search tree instance of the right node
            else:
                return self.right.contains(target)

    def get_max(self):
        """Returns the maximum number in the tree

        Returns:
            int -- the max number
        """
        # if there is no node to the right, return the current value of the node
        if self.right is None:
            return self.value

        # otherwise call the get_max method on the right node
        return self.right.get_max()

    def for_each(self, cb):
        """Calls the cb on every node in the tree

        Arguments:
            cb {func} -- the callback
        """
        # call cb on the root
        cb(self.value)

        # if there is a left node call the for_each method on the binary search tree instance of the left node
        if self.left is not None:
            self.left.for_each(cb)

        # if there is a right node call the for_each method on the binary search tree instance of the right node
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        print(node.value)

        if node.right is not None:
            self.stack.push(node.right)

        if node.left is not None:
            self.stack.push(node.left)

        if not self.stack.len():
            return
        self.in_order_print(self.stack.pop())

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # create the queue instance
        queue = Queue()
        # add the node to queue
        queue.enqueue(node)

        # while there is a node in the queue
        while queue.len():
            # dequeue the queue
            current_node = queue.dequeue()
            # print the value of the node
            print(current_node.value)

            # if there is a left node add it to the queue
            if current_node.left is not None:
                queue.enqueue(current_node.left)

            # if there is a right node add it to the queue
            if current_node.right is not None:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create the stack instance
        stack = Stack()
        # add the node to stack
        stack.push(node)

        # while there is a node in the stack
        while stack.len():
            # pop the stack
            current_node = stack.pop()
            # print the value of the node
            print(current_node.value)

            # if there is a left node add it to the stack
            if current_node.left is not None:
                stack.push(current_node.left)

            # if there is a right node add it to the stack
            if current_node.right is not None:
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
