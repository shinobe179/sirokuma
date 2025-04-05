from ..source import Source
from typing import IO

class File(Source):
    def __init__(self, path: str):
        self.path = path

    def crawl(self) -> IO[bytes]:
        file = open(self.path, mode='rb')
        return file
