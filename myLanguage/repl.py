from typing import List

from myLanguage.ast import Program
from myLanguage.lexer import Lexer
from myLanguage.parser import Parser
from myLanguage.token import (
    Token,
    TokenType,
)

EOF_TOKEN: Token = Token(TokenType.EOF, '')


def _print_parse_errors(errors: List[str]):
    for error in errors:
        print(error)

def start_repl() -> None:
    while (source := input('>> ')) != 'exit()':
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()

        if len(parser.errors) > 0:
            _print_parse_errors(parser.errors)
            continue

        print(program)


