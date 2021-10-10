from unittest import TestCase

from myLanguage.ast import (
    Identifier,
    LetStatement,
    Program,
    ReturnStatement,
)
from myLanguage.token import (
    Token,
    TokenType,
)


class ASTTest(TestCase):

    def test_let_statement(self) -> None:
        program: Program = Program(statements=[
            LetStatement(
                token=Token(TokenType.VAR, literal='var'),
                name=Identifier(
                    token=Token(TokenType.IDENTIFIER, literal='mi_var'),
                    value='mi_var'
                ),
                value=Identifier(
                    token=Token(TokenType.IDENTIFIER, literal='otra_variable'),
                    value='otra_var'
                )
            ),
        ])
        
        program_str = str(program)

        self.assertEquals(program_str, 'var mi_var = otra_var;')

    def test_return_statement(self) -> None:
        program: Program = Program(statements=[
            ReturnStatement(
                token=Token(TokenType.RETURN, literal='return'),
                return_value=Identifier(
                    token=Token(TokenType.IDENTIFIER, literal='mi_var'),
                    value='mi_var'
                )
            ),
        ])

        program_str = str(program)

        self.assertEquals(program_str, 'return mi_var;')