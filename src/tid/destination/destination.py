from abc import ABC, abstractmethod

# Destination is an interface of a destination of log.
class Destination(ABC):

    @abstractmethod
    def save(self):
        pass
