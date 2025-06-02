from __future__ import annotations

import sys
import os
node_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'parser')
sys.path.append(node_path)

from node import Node, NodeType

class Interpreter:

    """
        if the node is a literal node:
            the value of the expression is the literal constant(number) itself
        otherwise:
            let our operator be OP.
            Evaluate the left node. Let this value be `LEFT_VALUE`
            Evaluate the right node. Let this value be `RIGHT_VALUE`
            the value of the (binary) node would be LEFT_VALUE OP RIGHT_VALUE
    """
    @staticmethod
    def interpret(node: Node) -> int:
        if node.type == NodeType.NODE_LITERAL:
            return node.value
        
        else:
            left_value : int = Interpreter.interpret(node.left)
            right_value : int = Interpreter.interpret(node.right)

            if node.type == NodeType.NODE_ADD:
                return left_value + right_value

            elif node.type == NodeType.NODE_SUBTRACT:
                return left_value - right_value

            elif node.type == NodeType.NODE_MULTIPLY:
                return left_value * right_value
