from myLanguage.token import (
    Token, 
    TokenType
)

from myLanguage.lexer import Lexer

EOF_TOKEN = Token(TokenType.EOF, '')

def start_repl() -> None:
    while(source := input('>>')) != 'exit()':
        lexer: Lexer = Lexer(source)
        while(token := lexer.next_token()) != EOF_TOKEN:
            print(token)
