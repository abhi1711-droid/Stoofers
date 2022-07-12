import csv
import os

from static_data.models import Pincode


def run():
    with open("scripts/Pincode.csv") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            pincode = Pincode(pincode=row[4])

            pincode.save()
