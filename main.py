from __future__ import annotations
from typing import List
import sys
import os

from scanner.scanner import Scanner
from parser.parser import Parser, Node
from interpreter.interpreter import Interpreter
from exceptions.exceptions import ParserException, ScannerException, InterpreterException

def runFile() -> None:
    fileName : str = sys.argv[1]
    if not os.path.exists(fileName):
        print("[FileNotFoundError]: No such s-expression file found")
        sys.exit(1)

    with open(fileName, 'r') as in_file:
        input_source_code = in_file.read()
        runCode(input_source_code, file=True)

def runREPL() -> None:
    print("S-expression interpreter. Type `exit` to exit")
    print(">> ",end='')
    input_source_code = input()
    while input_source_code.strip().lower() != 'exit':
        runCode(input_source_code)
        print(">> ",end='')
        input_source_code = input()

def runCode(input_source_code: str, file: bool = False) -> None:
    error = False
    try:
        # Use the scanner to generate tokens based on the source code
        scanner: Scanner = Scanner(input_source_code)

        # Use the parser to generate parse tree(s)
        parser: Parser = Parser(scanner.tokens)
        nodes : List[Node] = parser.parse()

        for node in nodes:
            # Interpret each parse tree
            value = Interpreter.interpret(node)
            print(value)

    except ParserException as e:
        print(f'[ParserError]: {str(e)}')
        error = True
    except ScannerException as e:
        print(f'[ScannerError]: {str(e)}')
        error = True
    except InterpreterException as e:
        print(f'[InterpreterError]: {str(e)}')
        error = True
    except Exception as e:
        print(f'[UnknownError]: {str(e)}')
        error = True
    finally:
        if file and error:
            sys.exit(1)

    
def main() -> None:
    if len(sys.argv) == 1:
        # run the REPL 
        runREPL()

    elif len(sys.argv) == 2:
        # run the File
        runFile()

    else:
        print('[ArgumentError]: Provide no arguments for REPL, one argument to interpret s-expression file')
        sys.exit(1) 

if __name__ == "__main__":
    main()
