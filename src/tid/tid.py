from typing import List

from .stream import Stream

# TID manages stream processing.
class TID:

    def __init__(self, streams: List[Stream]):
        self.streams = streams

    def totte_irete_dasu(self, stream: Stream):
        stream.dst.save(stream.src.crawl())

    def run(self):
        for stream in self.streams:
                self.totte_irete_dasu(stream)

    def run_by_tag(self, tags: List[str]):
        for stream in self.streams:
            if tags in stream.tags:
                self.totte_irete_dasu(stream)
