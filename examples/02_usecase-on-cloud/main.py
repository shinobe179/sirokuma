import sirokuma
from sirokuma.source.file import File
from sirokuma.destination.stdout import Stdout
from sirokuma.stream import Stream


def main(event, context):
    # expected event: {"Tags": ["land", "sea"]}
    tags = event['Tags']

    poller = sirokuma.Sirokuma([
        Stream(
                File('land_animals.txt'),
                Stdout(),
                ['land'],
            ),
        Stream(
                File('sea_animals.txt'),
                Stdout(),
                ['sea'],
            ),
        Stream(
                File('sky_animals.txt'),
                Stdout(),
                ['sky'],
            ),
        ])

    poller.run_any_tags_matched(tags)
