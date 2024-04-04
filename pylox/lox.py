"""
Main language runner.
"""

from pathlib import Path
import readline

from .completion import Completer
from .scanner import Scanner
from .tokens import KEYWORDS


class Lox:
    def __init__(self) -> None:
        self.had_error = False

    def error(self, line: int, error: str) -> None:
        pass

    def report(self, line: int, where: str, message: str) -> None:
        pass

    def run(self, source: str) -> None:
        """
        Run script.

        Args:
            source:
                Entire script as multiline string.

        Return:
            None
        """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        # Just print tokens for now
        for token in tokens:
            print(repr(token))

    def run_file(self, path: Path) -> None:
        with open(path, 'rt') as fp:
            source = fp.read()
        self.run(source)

    def run_prompt(self) -> None:
        """
        Run REPL prompt.

        Use 'exit', 'quit', or ctrl+d to exit.

        Todo:
            Add identifiers to completer.
        """
        completer = Completer(KEYWORDS)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')

        while True:
            try:
                source = input('lox> ')
            except EOFError:
                break

            if source.casefold() in ('quit', 'exit'):
                break

            self.run(source)
