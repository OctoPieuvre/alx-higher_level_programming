#!/usr/bin/python3

"""Define the Node class"""

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
          self.__head = None

      def __str__(self):
          """Initialie an empty string to store the output."""

          result = []
          current = self.__head
          while current:
              result += str(current.data) + "\n"
              current = current.next_node

          return result

      def sorted_insert(self, value):
          """Create a new node with the given value"""

          new_node = Node(value)

          if self.__head is None:
              new_node.next_node = None
              self.__head = new_node
          elif value < self.__head.data:
              new_node.next_node = self.__head
              self.__head = new_node
          else:
              current = self.__head
              while current.next_node is not None and value > current.next_node.data:
                  current = current.next_node
              new_node.next_node = current.next_node
              current.next_node =new_node
                  
