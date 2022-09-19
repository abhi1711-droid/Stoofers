import csv
import os

from static_data.models import Pincode, City, State, Country


def run():
    with open("scripts/Pincode.csv", encoding="utf8") as file:
        reader = csv.reader(file)
        next(reader)
        Pincode.objects.all().delete()
        State.objects.all().delete()
        City.objects.all().delete()
        country = Country.objects.filter(name="India").first()
        for row in reader:
            print(row)
            state = row[4]
            city = row[3]
            pincode = row[1]
            state, created_s = State.objects.get_or_create(
                name=state.lower(), country_id=country.id
            )
            city, created_c = City.objects.get_or_create(name=city.lower(), state=state)
            pincode, created = Pincode.objects.get_or_create(
                pincode=int(pincode), city=city
            )
            print(f"{pincode}----{created}")
