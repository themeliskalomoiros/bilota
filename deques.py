class Deque:
    """An abstract data type that resembles both a stack and a queue.

    Items in a deque can be added to an removed from both the back and front.

    (FIFO and LIFO)
    """

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Takes an item as a parameter and inserts it into the 0th index of the
        list that is representing the Deque.

        The runtime is linear, or O(n), because every time you insert into the
        front of a list, all the other items in the list need to shift one
        position to the right.
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """Takes an item as a parameter and appends that item to the end of the
        list that is representing the Deque.

        The runtime is constant, or O(1), because appending at the end of the
        happens in constant time.
        """
        self.items.append(item)

    def remove_front(self):
        """Removes and returns the item in the 0th index of the list, which
        represents the front of the Deque.

        The runtime is linear, or O(n), because when we remove an item from the
        0th index all the other items have to shift one index to the left.
        """
        if self.items:
            return self.items.pop(0)

    def remove_rear(self):
        """Removes and returns the last item of the list, which represents the
        rear of the Deque.

        The runtime is constant, or O(1), because all we're doing is indexing to
        the end of a list.
        """
        if self.items:
            return self.items.pop()

    def peek_front(self):
        """Returns the value found at the -0th index of the list, which represents
        the front of the Deque.

        The runtime is constant because all we're doing is indexing into a list.
        """
        if self.items:
            return self.items[0]

    def peek_rear(self):
        """Returns the value found at the -1st index of the list, which represents
        the front of the Deque.

        The runtime is constant because all we're doing is indexing into a list.
        """
        if self.items:
            return self.items[-1]

    def size(self):
        """Returns the length of the list that is representing the Deque.

        This method runs in constant time because finding the length of a list
        also happens in constant time.
        """
        return len(self.items)

    def is_empty(self):
        """This method returns a boolean value describing whethere or not the
        Deque is empty.

        Testing for equality happens in constant time.
        """
        return self.items == []
