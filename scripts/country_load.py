import csv
from static_data.models import Country


def run():
    with open("scripts/countries.csv", encoding="utf8") as file:
        reader = csv.reader(file)
        next(reader)
        Country.objects.all().delete()
        for row in reader:
            Country.objects.get_or_create(name=row[1])
