
from unittest import TestCase

from pylox.completion import Completer


KEYWORDS = [
    'and', 'class', 'clock', 'false', 'fun',
    'nil', 'or', 'print', 'true', 'var', 'while',
]


class CompleterTest(TestCase):
    def setUp(self) -> None:
        self.completer = Completer(KEYWORDS)

    def test_complete_empty(self) -> None:
        """
        Empty string matches all words so that user can choose.
        """
        self.assertEqual(self.completer.complete('', 0), 'and')
        self.assertEqual(self.completer.complete('', 1), 'class')
        self.assertEqual(self.completer.complete('', 2), 'clock')
        self.assertEqual(self.completer.complete('', 9), 'var')
        self.assertEqual(self.completer.complete('', 10), 'while')
        self.assertEqual(self.completer.complete('', 11), None)

    def test_complete_no_match(self) -> None:
        """
        No match signaled by none.
        """
        match = self.completer.complete('shark', 0)
        self.assertIsNone(match)

    def test_complete_one_match(self) -> None:
        """
        Second call returns none.
        """
        match = self.completer.complete('a', 0)
        self.assertEqual(match, 'and')

        match = self.completer.complete('a', 1)
        self.assertIsNone(match)

    def test_complete_case_sensitive(self) -> None:
        """
        Matches are case-sensitive.
        """
        match = self.completer.complete('A', 0)
        self.assertIsNone(match)

    def test_complete_multiple_matches(self) -> None:
        """
        Matches should come out in order while 'state' incremented.
        """
        match = self.completer.complete('cl', 0)
        self.assertEqual(match, 'class')

        match = self.completer.complete('cl', 1)
        self.assertEqual(match, 'clock')

        match = self.completer.complete('cl', 2)
        self.assertIsNone(match)

    def test_add_existing(self) -> None:
        """
        Adding already existing words should be a no-op.
        """
        self.assertEqual(self.completer.words, KEYWORDS)
        self.completer.add('class')
        self.completer.add('class')
        self.assertEqual(self.completer.words, KEYWORDS)

    def test_add_new(self) -> None:
        """
        Ensure new words get added, and in order.
        """
        # If at first you don't succeed...
        match = self.completer.complete('shark', 0)
        self.assertIsNone(match)

        # ...lower your expectations!
        self.completer.add('sharknado')
        match = self.completer.complete('shark', 0)
        self.assertEqual(match, 'sharknado')

        # Peek behind curtains to check insertion order
        expected = [
            'and',
            'class',
            'clock',
            'false',
            'fun',
            'nil',
            'or',
            'print',
            'sharknado',
            'true',
            'var',
            'while',
        ]
        self.assertEqual(self.completer.words, expected)
