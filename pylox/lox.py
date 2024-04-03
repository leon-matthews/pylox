"""
Main language runner.
"""

from pathlib import Path


class Lox:
    def __init__(self) -> None:
        self.had_error = False

    def error(self, line: int, error: str) -> None:
        pass

    def report(self, line: int, where: str, message: str) -> None:
        pass

    def run(self, string: str) -> None:
        pass

    def run_file(self, path: Path) -> None:
        pass

    def run_prompt(self) -> None:
        pass
