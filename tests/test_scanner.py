
from unittest import TestCase

from pylox.scanner import Scanner
from pylox.tokens import Token, TokenType


class EmptySourceTest(TestCase):
    """
    Empty source, ie. hitting enter in interactive mode.
    """
    def test_at_end(self) -> None:
        scanner = Scanner("")
        self.assertTrue(scanner._at_end())

    def test_advance_error(self) -> None:
        scanner = Scanner("")
        message = r"^string index out of range$"
        with self.assertRaisesRegex(IndexError, message):
            scanner._advance()

    def test_scan_tokens(self) -> None:
        scanner = Scanner("")
        tokens = scanner.scan_tokens()
        self.assertEqual(repr(tokens), "[<Token:EOF>]")


class SingleCharacterTokensTest(TestCase):
    def test_at_end(self) -> None:
        scanner = Scanner(";")
        self.assertFalse(scanner._at_end())

    def test_advance(self) -> None:
        scanner = Scanner(";")
        self.assertFalse(scanner._at_end())
        char = scanner._advance()
        self.assertEqual(char, ';')
        self.assertTrue(scanner._at_end())

    def test_single_semicolon(self) -> None:
        scanner = Scanner(";")
        tokens = scanner.scan_tokens()
        expected = [
            '<Token:SEMICOLON>',
            '<Token:EOF>',
        ]
        self.assertEqual([repr(t) for t in tokens], expected)

    def test_single_semicolon_details(self) -> None:
        scanner = Scanner(";")
        tokens = scanner.scan_tokens()
        semicolon = tokens[0]
        expected = {
            'lexeme': ';',
            'line': 1,
            'literal': None,
            'type_': TokenType.SEMICOLON,
        }
        self.assertEqual(vars(semicolon), expected)

    def test_all_singles(self) -> None:
        scanner = Scanner("(){}.,-+;/*")
        tokens = [repr(t) for t in scanner.scan_tokens()]
        expected = [
            '<Token:LEFT_PAREN>',
            '<Token:RIGHT_PAREN>',
            '<Token:LEFT_BRACE>',
            '<Token:RIGHT_BRACE>',
            '<Token:DOT>',
            '<Token:COMMA>',
            '<Token:MINUS>',
            '<Token:PLUS>',
            '<Token:SEMICOLON>',
            '<Token:SLASH>',
            '<Token:STAR>',
            '<Token:EOF>',
        ]
        self.assertEqual(tokens, expected)

    def test_unexpected(self) -> None:
        scanner = Scanner("(%)")
        message = r"^Unexpected character: '%'$"
        with self.assertRaisesRegex(ValueError, message):
            scanner.scan_tokens()
