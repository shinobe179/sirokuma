from typing import List

from .stream import Stream

# Sirokuma manages stream processing.
class Sirokuma:

    def __init__(self, streams: List[Stream], dry_run: bool = False):
        self.dry_run = dry_run
        self.streams = streams

    def totte_irete_dasu(self, stream: Stream):
        if self.dry_run:
            print(f"Simulating: Saving data from {stream.src} to {stream.dst}")
        else:
            stream.dst.save(stream.src.crawl())

    def run_all(self, kakugo=False):
        if kakugo:
            for stream in self.streams:
                    self.totte_irete_dasu(stream)

    def run_all_tags_matched(self, tags: List[str]):
        for stream in self.streams:
            if all(tag in stream.tags for tag in tags):
                self.totte_irete_dasu(stream)

    def run_any_tags_matched(self, tags: List[str]):
        for stream in self.streams:
            if any(tag in stream.tags for tag in tags):
                self.totte_irete_dasu(stream)
