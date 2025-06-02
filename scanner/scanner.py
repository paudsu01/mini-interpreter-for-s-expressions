from __future__ import annotations
from typing import Iterator
from stoken import SToken, TType

# setting path to import ScannerException
import sys
import os
exceptions_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exceptions')
sys.path.append(exceptions_path)
from exceptions import ScannerException


class Scanner:


    def __init__(self, input_stream: str):
        self.__tokens = []
        self.__input_stream = input_stream
        self.__scan_tokens()


    """ 
        The main function for the scanner. 
        create all tokens based on the input source code
        raises ScannerException if unknown character
    """
    def __scan_tokens(self):
        # The core of the scanner is a loop !!
        # In this case, the loop can be simplified since there is a lot of repeating code like `index += 1` for multiple cases
        # However, for the sake of preserving the simplicity, I have chosen not to so that the reader can know exactly what is being done
        index : int = 0
        while (index < len(self.__input_stream)):

            current_char =  self.__input_stream[index]
            if (current_char in [' ', '\t', '\n']):
                # Ignore whitespace
                index += 1

            elif (current_char == '('):
                self.__add_token(index, index+1, TType.TOKEN_LEFT_PAREN)
                index += 1
                
            elif (current_char == ')'):
                self.__add_token(index, index+1, TType.TOKEN_RIGHT_PAREN)
                index += 1

            elif (current_char == '+'):
                self.__add_token(index, index+1, TType.TOKEN_ADD)
                index += 1

            elif (current_char == '-'):
                self.__add_token(index, index+1, TType.TOKEN_SUBTRACT)
                index += 1

            elif (current_char == '*'):
                self.__add_token(index, index+1, TType.TOKEN_MULTIPLY)
                index += 1

            elif (current_char in '0123456789'):
                start_index = index
                # Consume all the characters for our number value
                while (index < len(self.__input_stream) and self.__input_stream[index] in '0123456789'):
                    index += 1

                self.__add_token(start_index, index, TType.TOKEN_NUMBER)

            else:
                raise ScannerException("Unknown character")


    """ create a new Token and add the token to the tokens array """
    def __add_token(self, start_index: int, end_index: int, ttype: TType) -> None:
        token = SToken(self.__input_stream[start_index: end_index], ttype)
        self.__tokens.append(token)


    """ return the number of tokens """
    def __len__(self) -> int:
        return len(self.__tokens)


    """ get a token based on index """
    def __getitem__(self, index: int) -> SToken:
        if index >= len(self.__tokens):
            raise ScannerException("Scanner: Index error")
        else:
            return self.__tokens[index]

    def __iter__(self) -> Iterator:
        return iter(self.__tokens)

    @property
    def tokens(self):
        return self.__tokens
