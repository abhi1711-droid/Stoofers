import csv
from static_data.models import State


def run():
    with open("scripts/states.csv") as file:
        reader = csv.reader(file)
        next(reader)
        State.objects.all().delete()
        for row in reader:
            country = State(name=row[1], display_name=row[1], country_id=row[2])
            country.save()
