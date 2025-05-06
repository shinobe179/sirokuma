import sirokuma
from sirokuma.source.file import File
from sirokuma.destination.stdout import Stdout
from sirokuma.stream import Stream


poller = sirokuma.Sirokuma([
    Stream(
            File('land_animals.txt'),
            Stdout(),
            'land-animal_to_stdout',
            ['land'],
        ),
    Stream(
            File('sea_animals.txt'),
            Stdout(),
            'sea-animal_to_stdout',
            ['sea'],
        ),
    Stream(
            File('sky_animals.txt'),
            Stdout(),
            'sky-animal_to_stdout',
            ['sky'],
        ),
    ])

tags = ['land', 'sea']

print(f'# tags: {tags}')
print('# run_any_tags_matched runs streams matched ANY specified tags.')
poller.run_any_tags_matched(tags)

print('# run_all_tags_matched runs streams matched ALL specified tags.')
poller.run_all_tags_matched(tags)

print('# run_all runs all streams. You need kakuko to do that.')
poller.run_all(kakugo=True)
