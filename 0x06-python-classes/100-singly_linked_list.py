#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            new = Node(value, None)
            self.__head = new
        else:
            aux = self.__head
            while aux.next_node is not None and value > aux.next_node.data:
                aux = aux.next_node
            if aux.data < value:
                new = Node(value, aux.next_node)
                aux.next_node = new
            else:
                new = Node(value, aux)
                self.__head = new

    def __str__(self):
        s = ""
        while self.__head is not None:
            s = s + str(self.__head.data) + "\n"
            self.__head = self.__head.next_node
        return s[:-1]
