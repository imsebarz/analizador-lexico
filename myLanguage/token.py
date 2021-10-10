from enum import (
    auto,
    Enum,
    unique,
)

from typing import (NamedTuple, Dict, Any)

@unique
class TokenType(Enum):
    ASSING = auto()
    COMMA = auto()
    DIVIDE = auto()
    ELSE = auto()
    EOF = auto()
    EQUALS = auto()
    FALSE = auto()
    FLOAT = auto()
    FOR = auto()
    FUNCTION = auto()
    GT = auto()
    IDENTIFIER = auto()
    IF = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LBRACKET = auto()
    LPAREN = auto()
    LT = auto()
    MINUS = auto()
    MULTIPLY = auto()
    NEGATION = auto()
    NOT_EQUALS = auto()
    PLUS = auto()
    QUOTES = auto()
    RBRACE = auto()
    RBRAKET = auto()
    RETURN =  auto()
    RPAREN = auto()
    SEMICOLON = auto()
    STRING = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: Any

    def __str__(self) -> str:
        return (f'Type: {self.token_type.name}, Literal: {self.literal}')


def lookup_token_type(literal:Any) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'let': TokenType.VAR,
        'var': TokenType.VAR,
        'const': TokenType.VAR,
        'function': TokenType.FUNCTION,
        'return': TokenType.RETURN, 
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'false': TokenType.FALSE,
        'true': TokenType.TRUE,
        'for': TokenType.FOR,
        'while': TokenType.WHILE,
    }

    return keywords.get(literal, TokenType.IDENTIFIER)
