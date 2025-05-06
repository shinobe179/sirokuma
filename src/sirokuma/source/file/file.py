from ..source import Source

class File(Source):
    def __init__(self, path: str):
        self.path = path

    def crawl(self) -> bytes:
        file = open(self.path, mode='rb')
        return file.read()
