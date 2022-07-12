import csv
from static_data.models import Country


def run():
    with open("scripts/countries.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            a, b = Country.objects.get_or_create(name=row[1])
            print(a, b)
