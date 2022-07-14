import csv
from static_data.models import College, University, City, State, Country


def run():
    with open("scripts/Colleges.csv") as file:
        reader = csv.reader(file)
        next(reader)
        College.objects.all().delete()
        University.objects.all().delete()
        country = Country.objects.filter(name="India").first()
        for row in reader:
            college = row[0]
            city = row[10]
            state = row[11]
            university = row[7]
            state, created_s = State.objects.get_or_create(
                name=state, country_id=country.id
            )
            district, created_c = City.objects.get_or_create(name=city, state=state)
            print(district)
            university, created_u = University.objects.get_or_create(
                name=university, city_id=district.id
            )
            college, created = College.objects.get_or_create(
                name=college, university_id=university.id, city_id=district.id
            )
            print(f"{college}-----{created}")
