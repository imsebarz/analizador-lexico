from re import match
from myLanguage.token import (
    Token,
    TokenType, 
    lookup_token_type
)

class Lexer:
    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._position: int = 0
        self._read_position: int = 0

        self._read_character()

    def next_token(self) -> Token:
        self._skip_whitespace()
        if match(r'^\+$', self._character):
            token = Token(TokenType.PLUS, self._character)
        elif match(r'^\=$', self._character):
            if self._peak_character() == '=':
                token = self._make_two_character_token(TokenType.EQUALS)
            else:
                token = Token(TokenType.ASSING, self._character)
        elif match(r'^\/$', self._character):
            token = Token(TokenType.DIVIDE, self._character)
        elif match(r'^\-$', self._character):
            token = Token(TokenType.MINUS, self._character)
        elif match(r'^\<$', self._character):
            token = Token(TokenType.LT, self._character)
        elif match(r'^\!$', self._character):
            if self._peak_character() == '=':
                token = self._make_two_character_token(TokenType.NOT_EQUALS)
            else:
                token = Token(TokenType.NEGATION, self._character)
        elif match(r'^\>$', self._character):
            token = Token(TokenType.GT, self._character)
        elif match(r'^\*$', self._character):
            token = Token(TokenType.MULTIPLY, self._character)
        elif match(r'^\($', self._character):
            token = Token(TokenType.LPAREN, self._character)
        elif match(r'^\)$', self._character):
            token = Token(TokenType.RPAREN, self._character)
        elif match(r'^\[$', self._character):
            token = Token(TokenType.LBRACKET, self._character)
        elif match(r'^\]$', self._character):
            token = Token(TokenType.RBRAKET, self._character)
        elif match(r'^\{$', self._character):
            token = Token(TokenType.LBRACE, self._character)
        elif match(r'^\}$', self._character):
            token = Token(TokenType.RBRACE, self._character)
        elif match(r'^\;$', self._character):
            token = Token(TokenType.SEMICOLON, self._character)
        elif match(r'^\,$', self._character):
            token = Token(TokenType.COMMA, self._character)
        elif match(r'^\'$', self._character):
            if(self._peak_character() == '\''):
                token_type = TokenType.QUOTES
            else:
                token_type = TokenType.STRING
            literal = self._read_string()
            self._read_character()
            return Token(token_type, literal)

        elif self._is_letter(self._character):
            literal = self._read_identifier()
            token_type = lookup_token_type(literal)

            return Token(token_type, literal)

        elif self._is_number(self._character):
            literal = self._read_number()
            if(match(r'^\d+\.{1}\d+$', literal)):
                return Token(TokenType.FLOAT, literal)
            elif(match(r'^\d+$', literal)):
                return Token(TokenType.INT, literal)
            else:
                token = Token(TokenType.ILLEGAL, literal)

        elif match(r'^$', self._character):
            token = Token(TokenType.EOF, self._character)
        else:
            token = Token(TokenType.ILLEGAL, self._character)
            
        self._read_character()
        return token



    def _is_letter(self, character: str) -> bool:
        return bool(match(r'^[a-záéíóúñA-ZÁÉÍÓÚÑ_]$', character))

    def _is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character) or match(r'^\.$', character))

    def _read_identifier(self) -> str:
        initial_position = self._position
        while(self._is_letter(self._character)):
            self._read_character()
        return self._source[initial_position:self._position]

    def _read_number(self) -> str:
        initial_position = self._position
        while(self._is_number(self._character)):
            self._read_character()
        return self._source[initial_position:self._position]


    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1

    def _skip_whitespace(self):
        while(match(r'^[\s\t]$', self._character)):
            self._read_character()

    def _peak_character(self) -> str:
        if self._read_position >= len(self._source):
            return ''
        return self._source[self._read_position]

    def _make_two_character_token(self, token_type: TokenType) -> Token:
        prefix = self._character
        self._read_character()
        suffix = self._character

        return Token(token_type, f'{prefix}{suffix}')

    def _read_string(self) -> Token:
        initial_position = self._position
        self._read_character()
        while(match(r'[^\']', self._character)):
            while match(r'[\s\da-záéíóúñA-ZÁÉÍÓÚÑ_?¡¿@$%&#,.:;!""]',self._character):
            #  print(self._character)
             self._read_character()
        
        return self._source[initial_position:self._position + 1]
            