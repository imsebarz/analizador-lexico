from enum import (
    auto,
    Enum,
    unique,
)

from typing import (NamedTuple, Dict)

@unique
class TokenType(Enum):
    ASSING = auto()
    COMMA = auto()
    DIVIDE = auto()
    ELSE = auto()
    EOF = auto()
    EQUALS = auto()
    FALSE = auto()
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
    RBRACE = auto()
    RBRAKET = auto()
    RETURN =  auto()
    RPAREN = auto()
    SEMICOLON = auto()
    TRUE = auto()
    VAR = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return (f'Type: {self.token_type.name}, Literal: {self.literal}')


def lookup_token_type(literal:str) -> TokenType:
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
    }

    return keywords.get(literal, TokenType.IDENTIFIER)
