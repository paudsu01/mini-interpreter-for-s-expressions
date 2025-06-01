from __future__ import annotations
from typing import Union
from enum import Enum

# Define a Token class.
# A token instance should contain information like the type of the token and the value of the token (useful for tokens of type TOKEN_NUMBER as their value is necessary)
class Token:

    def __init__(self, value: str, token_type: TType):
        self.__value = value
        self.__token_type = token_type

    @property
    def value(self) -> Union[str, int]:
        return self.__value

    @property
    def type(self) -> TType:
        return self.__token_type


class TType(Enum):
    TOKEN_LEFT_PAREN = 0
    TOKEN_RIGHT_PAREN = 1
    TOKEN_ADD = 2
    TOKEN_SUBTRACT = 3
    TOKEN_MULTIPLY = 4 
    TOKEN_NUMBER = 5
