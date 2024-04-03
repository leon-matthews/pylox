
import builtins
from pprint import pprint


# Make pp() available globally for debugging
builtins.pp = pprint                                        # type: ignore[attr-defined]
