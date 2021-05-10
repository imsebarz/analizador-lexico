from unittest import TestCase
from myLanguage.lexer import Lexer
from typing import List
from myLanguage.token import (
    Token,
    TokenType
)

class LexerTest(TestCase):
    
    def test_illegal(self) -> None:
        source: str = '¿¡@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '@'),
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_one_character_operator(self) -> None:
        source: str = '=+-*/<>!'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSING, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.MULTIPLY, '*'),
            Token(TokenType.DIVIDE, '/'),
            Token(TokenType.LT, '<'),
            Token(TokenType.GT, '>'),
            Token(TokenType.NEGATION, '!'),
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_two_character_operators(self) -> None:
        source: str = '''
        10 == 10;
        10 != 9;
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())
            if(tokens[-1].token_type.name == TokenType.EOF.name):
                break

        expected_tokens: List[Token] = [
            Token(TokenType.INT, '10'),
            Token(TokenType.EQUALS, '=='),
            Token(TokenType.INT, '10'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.INT, '10'),
            Token(TokenType.NOT_EQUALS, '!='),
            Token(TokenType.INT, '9'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.EOF, ''),
        ]

        self.assertEquals(tokens, expected_tokens)
    
    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, ''),
        ]

    def test_delimiters(self) -> None:
        source: str = '()[]{};,'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACKET, '['),
            Token(TokenType.RBRAKET, ']'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.COMMA, ','),
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_assignment(self) -> None:
        source: str = 'let numerito = 5090;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())
            if(tokens[-1].token_type.name == TokenType.EOF.name):
                break

        expected_tokens: List[Token] = [
            Token(TokenType.VAR, 'let'),
            Token(TokenType.IDENTIFIER, 'numerito'),
            Token(TokenType.ASSING, '='),
            Token(TokenType.INT, '5090'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.EOF, ''),
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_function_declaration(self) -> None:
        source: str = '''let suma = function(x, y){
            return x + y; 
        };'''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())
            if(tokens[-1].token_type.name == TokenType.EOF.name):
                break

        expected_tokens: List[Token] = [
            Token(TokenType.VAR, 'let'),
            Token(TokenType.IDENTIFIER, 'suma'),
            Token(TokenType.ASSING, '='),
            Token(TokenType.FUNCTION, 'function'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENTIFIER, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENTIFIER, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.IDENTIFIER, 'x'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.IDENTIFIER, 'y'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.EOF, ''),
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_function_call(self) -> None:
        source:str = 'let result = suma(8,9)'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())
            if(tokens[-1].token_type.name == TokenType.EOF.name):
                break

        expected_tokens: List[Token] = [
            Token(TokenType.VAR, 'let'),
            Token(TokenType.IDENTIFIER, 'result'),
            Token(TokenType.ASSING, '='),
            Token(TokenType.IDENTIFIER, 'suma'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '8'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.INT, '9'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.EOF, ''),
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_control_statement(self) -> None:
        source:str = '''
        if(5 < 9) { 
            return true
        } else {
            return false
        }'''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())
            if(tokens[-1].token_type.name == TokenType.EOF.name):
                break

        expected_tokens: List[Token] = [
            Token(TokenType.IF, 'if'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '9'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.TRUE, 'true'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.ELSE, 'else'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.FALSE, 'false'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.EOF, ''),
        ]

        self.assertEquals(tokens, expected_tokens)


