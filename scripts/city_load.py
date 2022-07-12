import csv
from static_data.models import City


def run():
    with open("scripts/cities.csv") as file:
        reader = csv.reader(file)
        next(reader)
        City.objects.all().delete()
        for row in reader:
            country = City(name=row[1], display_name=row[1], state_id=row[2])
            country.save()
