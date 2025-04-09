from pydantic import ByteString
from logpolar import *

class StdIn(Source):

    def crawl(self):
        ret: ByteString = input('input: ').encode()
        return ret
