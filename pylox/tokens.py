
from enum import Enum
from typing import Any


class Token:
    Type = Enum('Type', (
        # Single character tokens
        'LEFT_PAREN RIGHT_PAREN LEFT_BRACE RIGHT_BRACE '
        'COMMA DOT MINUS PLUS SEMICOLON SLASH STAR '

        # One or two characters
        'BANG BANG_EQUAL EQUAL EQUAL_EQUAL '
        'GREATER GREATER_EQUAL LESS LESS_EQUAL '

        # Literals
        'IDENTIFIER STRING NUMBER '

        # Keywords
        'AND CLASS ELSE FALSE FUN FOR IF NIL OR '
        'PRINT RETURN SUPER THIS TRUE VAR WHILE '

        # Last!
        'EOF')
    )

    def __init__(self, type_: Type, lexeme: str, literal: Any, line: int):
        """
        Initialiser.

        Args:
            type:
                Type enum, eg. Token.Type.SEMICOLON
            lexeme:
                Original string from source
            literal:
                Native type of literal, None if not a literal.
            line:
                Line number where token found.

        """
        self.type_ = type_
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:{str(self)[1:-1]}>"

    def __str__(self) -> str:
        extra = ''
        if self.type_ is self.Type.IDENTIFIER:
            extra = f":{self.lexeme}"
        if self.literal is not None:
            extra = f":{self.literal}"
        return f"<{self.type_.name}{extra}>"
