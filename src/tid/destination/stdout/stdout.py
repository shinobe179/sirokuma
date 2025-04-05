import sys
from typing import IO
from ..destination import Destination

class Stdout(Destination):
    def save(self, data: IO[bytes]):
        sys.stdout.buffer.write(data.read())
