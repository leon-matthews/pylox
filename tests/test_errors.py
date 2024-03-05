from unittest import TestCase

from pylox.errors import ErrorReporter, ErrorType


class TestToken(TestCase):
    def test_has_errors_false(self) -> None:
        reporter = ErrorReporter()
        self.assertFalse(reporter.has_errors())

    def test_has_errors_true(self) -> None:
        reporter = ErrorReporter()
        reporter.report(14, ErrorType.SYNTAX)
        self.assertTrue(reporter.has_errors())
