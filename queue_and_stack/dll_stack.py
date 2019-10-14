from doubly_linked_list import DoublyLinkedList


class Stack:
    """Implementation of the Stack data structure
    using a doubly linked list  as the storage
    """

    def __init__(self):
        """Initiate the stack with size 0 and the DoublyLinkedList as storage
        """
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        """Pushes an node onto the stack using the add_to_head method of the DoublyLinkedList instance

        Arguments:
            value {any} -- value to be pushed
        """
        # use the add_to_head method on the DoublyLinkedList instance passing the value
        self.storage.add_to_head(value)
        # increment the length
        self.size += 1

    def pop(self):
        """Pops nodes from the stack using the remove_from_head on the DoublyLinkedList instance

        Returns:
            any -- the value that was popped
        """
        # if length is zero return none
        if not self.size:
            return None

        # use the remove_from_head method on the DoublyLinkedList instance
        popped_value = self.storage.remove_from_head()
        # decrement the length
        self.size -= 1
        # return the value popped
        return popped_value

    def len(self):
        """Returns the current size of the stack

        Returns:
            int -- size of the stack
        """
        return self.size
