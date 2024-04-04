
from unittest import mock, TestCase

from pylox.lox import Lox


class LoxRunPromptTest(TestCase):
    """
    Test the interactive REPL - as best we can!
    """
    @mock.patch('pylox.lox.input', create=True)
    def test_exit(self, input_mock) -> None:
        """
        Mock `input()` function to exit
        """
        input_mock.side_effect = ['EXIT', 'exit', 'QUIT', 'quit']
        lox = Lox()
        self.assertEqual(0, lox.run_prompt())               # EXIT
        self.assertEqual(0, lox.run_prompt())               # exit
        self.assertEqual(0, lox.run_prompt())               # QUIT
        self.assertEqual(0, lox.run_prompt())               # quit

        # Mock all used up?
        self.assertEqual(list(input_mock.side_effect), [])
