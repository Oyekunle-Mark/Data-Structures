from doubly_linked_list import DoublyLinkedList


class Queue:
    """Implementation of the Queue data structure using a DoublyLinkedList

    This implementation uses the tail of the DoublyLinkedList as the back of the queue and the head of the DoublyLinkedList as the front
    """

    def __init__(self):
        """Initializes the queue to an empty DoublyLinkedList and a size of zero
        """
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        """Enqueue the queue with a new node of value value

        Arguments:
            value {any} -- value to be enqueued
        """
        # enqueue using the add_to_tail method on the DoublyLinkedList instance
        self.storage.add_to_tail(value)
        # increment the size
        self.size += 1

    def dequeue(self):
        """Dequeue the node at the front of the queue

        Returns:
            any -- the item at the front
        """
        # if size is zero return None
        if not self.size:
            return None
        # dequeue using the remove_from_head method on the DoublyLinkedList instance
        value = self.storage.remove_from_head()
        # decrease the size
        self.size -= 1
        # return the value
        return value

    def len(self):
        """Returns the size of the queue

        Returns:
            int -- size of queue
        """
        return self.size
