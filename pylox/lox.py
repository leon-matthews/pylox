"""
Main language runner.
"""

from pathlib import Path
import readline
import sys

from .completion import Completer
from .scanner import Scanner
from .tokens import KEYWORDS


class Lox:
    def __init__(self) -> None:
        self.had_error = False

    def error(self, line: int, message: str) -> None:
        self.report(line, "", message)

    def report(self, line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        self.had_error = True

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

    def run_file(self, path: Path) -> int:
        """
        Open and run script file.

        Args:
            path:
                Path to UTF-8 script file.

        Returns:
            Error code, zero on normal exit.
        """
        with open(path, 'rt', encoding='utf-8') as fp:
            source = fp.read()
        self.run(source)

        error_code = 1 if self.had_error else 0
        return error_code

    def run_prompt(self) -> int:
        """
        Run REPL prompt.

        Use 'exit', 'quit', or ctrl+d to exit.

        Todo:
            Add identifiers to completer.

        Returns:
            Error code, zero on normal exit.
        """
        completer = Completer(KEYWORDS)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')

        while True:
            try:
                source = input('lox> ')
            except EOFError:
                return 0

            if source.casefold() in ('quit', 'exit'):
                return 0

            self.run(source)

        # Unexpected exit
        return 1
