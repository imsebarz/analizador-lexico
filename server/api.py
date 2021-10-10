from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from myLanguage.ast import Program
from myLanguage.lexer import Lexer
from myLanguage.parser import Parser
from myLanguage.token import (
    Token,
    TokenType,
)

from server.functions import (
    lexical_process,
    parsing_process,
)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://analizador-lexico.netlify.app/",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/process", tags=["process"])
async def process(data: dict) -> dict:

    tokens = lexical_process(data["source"])
    [errors, program] = parsing_process(data["source"])
    return {
        "tokens": tokens,
        "program": program,
        'errors': errors, 
    }
