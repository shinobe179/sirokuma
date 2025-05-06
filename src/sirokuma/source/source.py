from abc import ABC, abstractmethod

class Source(ABC):
    """Source is an interface of source of log file.
    """
    @abstractmethod
    def crawl(self) -> bytes:
        pass
