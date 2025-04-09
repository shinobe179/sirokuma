from typing import List

from sirokuma.source import Source
from sirokuma.destination import Destination


class Stream:
    """Stream is a management unit of Source and Destination.
       Stream can select processing streams by tags.
    """

    def __init__(self, src: Source, dst: Destination, tags: List[str]):
        """constructor of Stream.

        Args:
            src (sirokuma.Source):
            dst (sirokuma.Destination):
        """        
        self.src  = src
        self.dst  = dst
        self.tags = tags

    def with_tags(self, tags: List[str]):
        """with_tags desginates tags of stream.

        Args:
            tags (List[str]): 
        """        
        self.tags = tags
