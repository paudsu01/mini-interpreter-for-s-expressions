from __future__ import annotations
from typing import List, Tuple
from node import Node, LiteralNode, BinaryNode, NodeType

import sys
import os
scanner_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scanner')
exceptions_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exceptions')
sys.path.append(scanner_path)
sys.path.append(exceptions_path)

from stoken import SToken, TType
from scanner import Scanner
from exceptions import ParserException


class Parser:

    def __init__(self, tokens: List[SToken]):
        self.__tokens = tokens
        self.__current_token_index = 0

    def parse(self) -> Node:
        return self.__expr()

    """ Main parsing functions to implement recursive descent parsing """

    """ 
        We can actually reduce our production rules to just two !

        expr -> "(" (+|-|*) expr expr ")" | literal
    """
    def __expr(self) -> Node:

        if (self.__match_token(TType.TOKEN_LEFT_PAREN)):
            # This must mean our production rule is now
            # expr -> "(" (+|-|*) expr expr ")"
            
            # Consume the operator and get the NodeType value based on that
            node_type : NodeType = self.__operator()

            # Now, you get why the parsing is called recusrive descent !
            left_node : Node = self.__expr()
            right_node : Node = self.__expr()

            self.__consume_token(TType.TOKEN_RIGHT_PAREN)

            return BinaryNode(node_type, left_node, right_node)

        else:
            # Since we don't have a '(' as the first token, we must have a literal constant
            return self.__literal()

    """ literal -> [0-9]+ """
    def __literal(self) -> Node:
        # Our scanner already has a number token with the required value
        # So, let us create a LiteralNode with that value

        # Get the current token
        token : SToken = self.__tokens[self.__current_token_index]

        # Check if the current token is of number token type and consume if so
        self.__consume_token(TType.TOKEN_NUMBER)

        # Create a node for the parse tree and return
        return LiteralNode(NodeType.NODE_LITERAL, int(token.value))

    """
        Unlike __literal and __expr, the __operator method doesn't return a tree node, instead it just
        tries to consume a operator and returns the valid NodeType
    """
    def __operator(self) -> NodeType:
        token : SToken = self.__tokens[self.__current_token_index]

        self.__consume_token(TType.TOKEN_ADD, TType.TOKEN_SUBTRACT, TType.TOKEN_MULTIPLY)

        if (token.type == TType.TOKEN_ADD):
            return NodeType.NODE_ADD
        elif (token.type == TType.TOKEN_SUBTRACT):
            return NodeType.NODE_SUBTRACT
        else:
            return NodeType.NODE_MULTIPLY


    """ Helper functions """

    # Consume a SToken
    def __consume_token(self, *token_types: Tuple[TType]) -> None:

        if (self.__current_token_index >= len(self.__tokens)):
            raise ParserException("Out of tokens to consume")

        else:
            token : SToken = self.__tokens[self.__current_token_index]

            if (token.type in token_types):
                self.__current_token_index += 1

            else:
                raise ParserException(f'Expected {", ".join([i.value for i in token_types])}, got {token.value}')

    # Consume the token if it matches, do nothing otherwise
    def __match_token(self, token_type: TType) -> bool:

        token : SToken = self.__tokens[self.__current_token_index]

        if (token_type == token.type):
            self.__consume_token(token_type)
            return True
        return False
