from abc import ABC, abstractmethod
from typing import IO

class Destination(ABC):
    """Destination is an interface of a destination of log.
    """
    @abstractmethod
    def save(self, data: IO[bytes]):
        pass
