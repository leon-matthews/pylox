"""
Scanner produces list of tokens from program source.
"""

from typing import Any

from .tokens import SINGLE_CHARACTER_TOKENS, Token, TokenType


class Scanner:
    source: str
    tokens: list[Token]

    def __init__(self, source: str):
        """
        Initialiser.

        Args:
            source:
                Program source as simple string.
        """
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []

    def scan_tokens(self) -> list[Token]:
        """
        Scan entire source and produce list of tokens.

        Returns:
            List of token objects.
        """
        # Keep scanning
        while not self._at_end():
            self.start = self.current
            self._scan_token()

        # Add an EOF
        self._add_token(TokenType.EOF)
        return self.tokens

    def _add_token(self, type_: TokenType, literal: Any = None) -> None:
        text = self.source[self.start:self.current]
        token = Token(type_, text, literal, self.line)
        self.tokens.append(token)

    def _advance(self) -> str:
        """
        Move state forwards, fetch next character.

        Raises:
            IndexError:
                If source has already been consumed.

        Returns:
            The next single-character string.
        """
        char = self.source[self.current]
        self.current += 1
        return char

    def _at_end(self) -> bool:
        return self.current >= len(self.source)

    def _scan_token(self) -> None:
        """
        Extract current token, moving state forwards.
        """
        c = self._advance()
        match c:
            # Single character
            case c if c in SINGLE_CHARACTER_TOKENS:
                self._add_token(SINGLE_CHARACTER_TOKENS[c])

            # Default
            case _:
                raise ValueError(f"Unexpected character: {c!r}")
