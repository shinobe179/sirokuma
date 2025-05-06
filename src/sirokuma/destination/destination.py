from abc import ABC, abstractmethod

class Destination(ABC):
    """Destination is an interface of a destination of log.
    """
    @abstractmethod
    def save(self, data: bytes):
        pass
