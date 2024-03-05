
import sys

from .command import CommandLine


if __name__ == '__main__':
    command = CommandLine(sys.argv[1:])
    sys.exit(command.main())
