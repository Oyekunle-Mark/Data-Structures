from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        # state the limit of node the lru cache can hold
        self.limit = limit
        # track the current number of node it is holding
        self.node_count = 0
        # create a linked list to hold the key and basically create the order of the lru cache
        self.cache_list = DoublyLinkedList()
        # create a storage dict for fast acccess to node an d value in the cache
        # this will map the key to the value it holds and the node it is represented by in the linked list
        self.cache_storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if the key does not exist in the cache_storage return None
        if key not in self.cache_storage:
            return None

        # otherwise return the value associated with the key and move the node to the head of the cache_list
        else:
            # get the node associated with that key
            node = self.cache_storage[key]["node"]
            # move it to the front of the list as the most recently used value
            self.cache_list.move_to_front(node)

            # return the value associated with the key
            return self.cache_storage[key]["value"]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if the key exist in the cache_storage, replace its value and move the node to the head in the cache_list
        if key in self.cache_storage:
            # update the value that key is mapped to
            self.cache_storage[key]["value"] = value
            # fetch the node it is mapped to
            key_node = self.cache_storage[key]["node"]
            # move the node to the front of the list
            self.cache_list.move_to_front(key_node)
        # otherwise, check if the length of the node is up to the limit
        else:
            if self.node_count == self.limit:
                # if it is, delete the tail of the cache_list and remove the key value pair from the cache_storage
                popped_key = self.cache_list.remove_from_tail()
                # remove the key from the cache storage
                self.cache_storage.pop(popped_key)
                # add the new key value pair to the cache_storage and cache_list head
                node = self.cache_list.add_to_head(key)
                self.cache_storage[key] = {"value": value, "node": node}
            # if the length is not up to the limit, simply add the new key value pair to the cache_storage and cache_list head and increment node_count
            else:
                node = self.cache_list.add_to_head(key)
                self.cache_storage[key] = {"value": value, "node": node}
                self.node_count += 1
