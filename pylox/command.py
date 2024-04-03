
import argparse
import logging
from pathlib import Path
import time
from typing import Iterator

from .lox import Lox

logger = logging.getLogger(__name__)


def argparse_existing_file(string: str) -> Path:
    """
    An `argparse` type to convert string to a `Path` object.

    Raises `argparse.ArgumentTypeError` if path does not exist.
    """
    path = Path(string).expanduser().resolve()
    error = None
    if not path.exists():
        error = f"File does not exist: {path}"
    if not path.is_file():
        error = f"Path is not a file: {path}"

    if error is not None:
        raise argparse.ArgumentTypeError(error)
    return path


class CommandLine:
    """
    Start PyLox from command-line.
    """
    def __init__(self, args: list[str]):
        self.options = self.parse_options(args)
        pp(self.options)
        self.setup_logging()

    def main(self) -> int:
        lox = Lox()
        if self.options.file:
            lox.run_file(self.options.file)
        else:
            lox.run_prompt()
        return 0

    def parse_options(self, args: list[str]) -> argparse.Namespace:
        script_name = Path(__file__).parent.name
        parser = argparse.ArgumentParser(description='Lox Interpreter', prog=script_name)
        parser.add_argument(
            'file',
            metavar='FILE',
            nargs='?',
            type=argparse_existing_file,
            help="Script file")
        options = parser.parse_args(args)
        return options

    def setup_logging(self) -> None:
        logging.basicConfig(
            force=True,
            format="{levelname}: {message}",
            level=logging.DEBUG,
            style='{',
        )
