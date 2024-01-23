#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """
    Class representing a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a node with the given data and next_node reference.

        Args:
            data: The data to be stored in the node.
            next_node: Reference to the next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value: The data value to be set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node.

        Returns:
            The reference to the next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Args:
            value: Reference to the next node (Node object) or None.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Class representing a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new node with the given value into the sorted position

        Args:
            value: The value to be inserted.

        Note:
            The linked list is sorted in increasing order.
        """
        new_node = Node(value)

        if self.head is None:
            # If the list is empty, make the new node the head
            self.head = new_node
        elif value < self.head.data:
            # If the new node should be inserted at the beginning
            new_node.next_node = self.head
            self.head = new_node
        else:
            # Traverse the list to find the correct position to insert
            current = self.head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node

            # Insert the new node between the current node and the next node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            A string representing the linked list, with each node's data
        """
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next_node
        return '\n'.join(nodes)
