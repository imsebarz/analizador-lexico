from myLanguage.ast import Program
from myLanguage.lexer import Lexer
from myLanguage.parser import Parser
from myLanguage.token import (
    Token,
    TokenType,
)

EOF_TOKEN = Token(TokenType.EOF, '')


def lexical_process(source):
    lexer: Lexer = Lexer(source)
    listOfTokens = []
    while(token := lexer.next_token()) != EOF_TOKEN:
            listOfTokens.append({"type": token.token_type.name, "literal": token.literal})

    listOfTokens.append({"type": token.token_type.EOF, "literal": ""})
    return listOfTokens


def parsing_process(source):
    lexer: Lexer = Lexer(source)
    parser: Parser = Parser(lexer)
    program: Program = parser.parse_program()
    
    return (parser.errors, program)
