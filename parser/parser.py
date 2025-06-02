from __future__ import annotations
from typing import List
from node import Node, LiteralNode, BinaryNode, NodeType

import sys
sys.path.append("../scanner/")
sys.path.append("../exceptions/")

from stoken import SToken, TType
from exceptions import ParserException


class Parser:

    def __init__(self, tokens: List[SToken]):
        self.__tokens = tokens
        self.__current_token_index = 0

    def parse(self) -> Node:
        return self.__parseExpr()

    """ Main parsing functions to implement recursive descent parsing """

    """ 
        We can actually reduce our production rules to just two !

        expr -> "(" (+|-|*) expr expr ")" | literal
    """
    def __expr(self) -> Node:

        if self.__match_token(TType.TOKEN_LEFT_PAREN):
            # This must mean our production rule is now
            # expr -> "(" (+|-|*) expr expr ")"
            
            # TODO
            self.__consume_token(TType.TOKEN_RIGHT_PAREN)

        else:
            # Since we don't have a '(' as the first token, we must have a literal constant
            return self.__literal()

    """ literal -> [0-9]+ """
    def __literal(self) -> Node:
        # Our scanner already has a number token with the required value
        # So, let us create a LiteralNode with that value

        # Get the current token
        token = self.__tokens[self.__current_token_index]

        # Check if the current token is of number token type and consume if so
        self.__consume_token(TType.TOKEN_NUMBER)

        # Create a node for the parse tree and return
        return LiteralNode(NodeType.NODE_LITERAL, int(token.value))


    """ Helper functions """

    # Consume a SToken
    def __consume_token(self, token_type: TType) -> None:
        token = self.__tokens[self.__current_token_index]
        if (token_type == token.type):
            self.__current_token_index += 1
        else:
            raise ParserException(f'Expected {token_type.value}, got {token.value}')

    # Consume the token if it matches, do nothing otherwise
    def __match_token(self, token_type: TType) -> None:
        token = self.__tokens[self.__current_token_index]
        if (token_type == token.type):
            self.__consume_token()
