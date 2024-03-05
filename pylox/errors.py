
from __future__ import annotations

from dataclasses import dataclass

from enum import unique, StrEnum


@dataclass
class Error:
    line: int
    type_: ErrorType
    extra: str = ''


class ErrorReporter:
    def __init__(self) -> None:
        self.errors: list[Error] = []

    def has_errors(self) -> bool:
        return bool(self.errors)

    def report(self, line: int, type_: ErrorType, extra: str = '') -> None:
        """
        Report an error.

        Args:
            line:
                Line number where error found. Use 1 for REPL.
            type_:
                Type of error, eg. `ErrorType.SYNTAX`
            extra:
                Optional extra information.

        Returns:
            None
        """
        error = Error(line, type_, extra)
        self.errors.append(error)


@unique
class ErrorType(StrEnum):
    SYNTAX = 'Syntax Error'
