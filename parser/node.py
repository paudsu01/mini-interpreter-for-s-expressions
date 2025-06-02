from __future__ import annotations
from enum import Enum

class NodeType(Enum):
    NODE_ADD = '+'
    NODE_SUBTRACT = '-'
    NODE_MULTIPLY = '*'
    NODE_LITERAL = 'NUMBER'

class Node:


    def __init__(self, node_type: NodeType):
        self.__node_type = node_type
    

    @property
    def type(self):
        return self.__node_type


class BinaryNode(Node):

    def __init__(self, node_type: NodeType, left: Node, right: Node):
        super().__init__(node_type)
        self.__left = left
        self.__right = right

    """ Getters only ( no setters ) """
    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right


    """ Method to print the node as s-expression """
    def __repr__(self):
        return f'( {self.type.value} {self.left} {self.right} )'

class LiteralNode(Node):
    
    def __init__(self, node_type: NodeType, value: int):
        super().__init__(node_type)
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value

    """ Method to print the node as s-expression """
    def __repr__(self) -> str:
        return str(self.__value)

    def __str__(self) -> str:
        return repr(self)


