import tid
from tid.source import File
from tid.destination import Stdout
from tid.stream import Stream

porter = tid.TID([
        Stream(
            File('test.txt'),
            Stdout(),
            ['test']
        )
        ])

porter.run()
