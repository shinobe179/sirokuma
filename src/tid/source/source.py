from typing import IO
from abc import ABC, abstractmethod

# Source is an interface of source of log file.
class Source(ABC):

    @abstractmethod
    def crawl(self) -> IO[bytes]:
        pass
