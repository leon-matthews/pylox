
import argparse
import logging
from pathlib import Path
import time
from typing import Iterator


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
        self.setup_logging()

    def main(self) -> int:
        start = time.perf_counter()
        count = 0
        lines = self.readlines()
        elapsed = (time.perf_counter() - start) * 1000
        logger.debug(f"Ran for {elapsed:.1f}ms")
        return 0

    def parse_options(self, args: list[str]) -> argparse.Namespace:
        script_name = Path(__file__).parent.name
        parser = argparse.ArgumentParser(description='Lox Interpreter', prog=script_name)
        parser.add_argument(
            'file',
            metavar='FILE',
            type=argparse_existing_file,
            help="Script file")
        options = parser.parse_args(args)
        return options

    def readlines(self) -> Iterator[str]:
        path = self.options.file
        logger.debug(f"Reading lines from: {path}")
        num_lines = 0
        with open(path) as fp:
            for line in fp:
                num_lines += 1
                yield line.strip()
        logger.debug(f"Read {num_lines:,} lines from: {path.name}")

    def setup_logging(self) -> None:
        level = logging.DEBUG
        logging.basicConfig(
            force=True,
            format="{levelname}: {message}",
            level=level,
            style='{',
        )
