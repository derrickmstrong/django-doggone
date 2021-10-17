from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from detectiveagency.models import LostPet, Siblings
from pytz import UTC

DATETIME_FORMAT = '%m/%d/$Y %H:%M'

SIBLINGS_NAMES = [
    'Money',
    'Gizmo',
    'Sasha',
    'Snoopy'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables
"""

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our LostPet model"

    def handle(self, *args, **options):
        if Siblings.objects.exists() or LostPet.objects.exists():
            print('Pet data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Creating sibling data')
        for sibling_name in SIBLINGS_NAMES:
            sib = Siblings(name=sibling_name)
            sib.save()
        print('Loading pet data for lost pets')
        for row in DictReader(open('./pet_data.csv')):
            pet = LostPet()
            pet.name = row['Pet']
            pet.breed = row['Breed']
            pet.sex = row['Sex']
            pet.age = row['Age']
            pet.description = row['Description']
            raw_lost_date = row['Lost Date']
            lost_date = UTC.localize(datetime.strptime(raw_lost_date, DATETIME_FORMAT))
            pet.lost_date = lost_date
            pet.save()
            raw_sibling_names = row['Siblings']
            sibling_names = [name for name in raw_sibling_names.split(' | ') if name]
            for sib_name in sibling_names:
                sib = Siblings.objects.get(name=sib_name)
                pet.siblings.add(sib)
            pet.save()
