"""
Tab-completion of tokens and keywords in the REPL, powered by readline.
"""


class Completer:
    """
    Class-based completion function for readline module.

    Use to provide custom tab-completion of words while using a readline-
    powered prompt. Words to complete can be provided both during creation
    and later during operation.

    Install the completion function by calling readline's module-level
    functions::

        completer = Completer(['list', 'of', 'keywords')
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')

    Extra words to complete can be added at any time::

        completer.add('print')

    There's loads of room for optimisation (a radix trie?), and some interesting
    edge-cases (matches cache) to play around with, but I must resist the
    urge to over-engineer!
    """
    def __init__(self, words: list[str]|None) -> None:
        """
        Initialiser.

        Args:
            words:
                Initial set of words for completion list.
        """
        # Copy word list and keep it sorted.
        self.words = [] if words is None else list(words)
        self.words.sort()

        # Current set of matches. Not thread-safe.
        self._matches: list[str] = []

    def add(self, word: str) -> None:
        """
        Add word to list of completions.

        Args:
            word:

        """
        # Ignore repeats
        if word in self.words:
            return

        # Luckily, Python sorts already sorted lists very fast indeed.
        self.words.append(word)
        self.words.sort()

    def complete(self, text: str, state: int) -> str|None:
        """
        Callback function called by readline module.

        The readline module keeps calling this function with increasing
        values of `state` until a None is returned, signalling no more
        matches. For this reason we cache the current matches found.

        Args:
            text:
                Prefix to search for.
            state:
                Zero-based index of number of times function called for this
                match.

        Returns:
            Word to complete, none if matches exhausted.
        """
        # Find possible matches on first call
        if state == 0:
            self._matches = self._find_matches(text)

        # Look-up and return next match
        response = None
        try:
            response = self._matches[state]
        except IndexError:
            pass
        return response

    def _find_matches(self, text: str) -> list[str]:
        """
        Search words to generate list of matches.
        """
        # Empty match, return all
        if not text:
            return self.words[:]

        # Search by prefix
        matches = [word for word in self.words if word.startswith(text)]
        return matches
