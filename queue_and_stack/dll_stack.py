from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        # set the length to zero
        self.length = 0

    def push(self, value):
        # use the add_to_head method on the DoublyLinkedList instance passing the value
        self.storage.add_to_head(value)
        # increment the length
        self.length += 1

    def pop(self):
        # if length is zero return none
        if not self.length:
            return None

        # use the remove_from_head method on the DoublyLinkedList instance
        popped_value = self.storage.remove_from_head()
        # decrement the length
        self.length -= 1
        # return the value popped
        return popped_value

    def len(self):
        return self.length
