from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from myLanguage.token import (
    Token, 
    TokenType
)

from myLanguage.lexer import Lexer

app = FastAPI()
EOF_TOKEN = Token(TokenType.EOF, '')

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/process", tags=["process"])
async def add_todo(data: dict) -> dict:
    source = data["source"]
    lexer: Lexer = Lexer(source)
    listOfTokens = []
    while(token := lexer.next_token()) != EOF_TOKEN:
            listOfTokens.append({"type": token.token_type.name, "literal": token.literal})
    
    listOfTokens.append({"type": EOF_TOKEN.token_type.name, "literal": EOF_TOKEN.literal})

    return {
        "data": listOfTokens
    }