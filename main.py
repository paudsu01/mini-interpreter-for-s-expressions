from __future__ import annotations
from typing import List
import sys
import os

from scanner.scanner import Scanner
from parser.parser import Parser, Node
from interpreter.interpreter import Interpreter

def runFile() -> None:
    fileName : str = sys.argv[1]
    if not os.path.exists(fileName):
        raise FileNotFoundError("No such s-expression file found")

    with open(fileName, 'r') as in_file:
        input_source_code = in_file.read()
        runCode(input_source_code)

def runREPL() -> None:
    print("S-expression interpreter. Type `exit` to exit")
    print(">> ",end='')
    input_source_code = input()
    while input_source_code != 'exit':
        runCode(input_source_code)
        print(">> ",end='')
        input_source_code = input()

def runCode(input_source_code: str) -> None:
    # Use the scanner to generate tokens based on the source code
    scanner: Scanner = Scanner(input_source_code)

    # Use the parser to generate parse tree(s)
    parser: Parser = Parser(scanner.tokens)
    nodes : List[Node] = parser.parse()

    for node in nodes:
        # Interpret each parse tree
        value = Interpreter.interpret(node)
        print(value)
    
def main() -> None:
    if len(sys.argv) == 1:
        # run the REPL 
        runREPL()

    elif len(sys.argv) == 2:
        # run the File
        runFile()

    else:
        # error, expected 1 argument or 0
        pass
        # TODO

if __name__ == "__main__":
    main()
