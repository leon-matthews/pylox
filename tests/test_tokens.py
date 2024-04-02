
from unittest import TestCase

from pylox.tokens import Token, TokenType


class TestToken(TestCase):
    def test_repr(self) -> None:
        t = Token(TokenType.LEFT_PAREN, '(', None, 1)
        self.assertEqual(repr(t), '<Token:LEFT_PAREN>')

    def test_repr_identifier(self) -> None:
        t = Token(TokenType.IDENTIFIER, 'apple', None, 2)
        self.assertEqual(repr(t), '<Token:IDENTIFIER:apple>')

    def test_str(self) -> None:
        t = Token(TokenType.LEFT_PAREN, '(', None, 1)
        self.assertEqual(str(t), '<LEFT_PAREN>')

    def test_str_identifier(self) -> None:
        t = Token(TokenType.IDENTIFIER, 'apple', None, 2)
        self.assertEqual(str(t), '<IDENTIFIER:apple>')

    def test_str_string(self) -> None:
        t = Token(TokenType.STRING, "'banana'", 'banana', 3)
        self.assertEqual(str(t), "<STRING:banana>")

    def test_str_number(self) -> None:
        t = Token(TokenType.NUMBER, "33.3", 33.3, 4)
        self.assertEqual(str(t), "<NUMBER:33.3>")


class TestTokenType(TestCase):
    def test_enums(self) -> None:
        enums = list(TokenType)
        self.assertEqual(len(enums), 39)
