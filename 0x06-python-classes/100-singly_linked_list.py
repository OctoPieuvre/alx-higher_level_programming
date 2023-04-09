#!/usr/bin/python3

class Node:
      """Represent a node in a singly-linked list."""

      def __init__(self, data, next_node=None):
          """Initialize a new node

          Args:
            data (int): the data of the new node
            next_node (Node): The next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of the data of the Node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter of the node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter of the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of the next node"""
        if value is not None or type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
      """Represent a singly-linked list."""

      def __init__(self):
          """Initalize a new SinglyLinkedList."""
          self.head = None
