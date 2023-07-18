import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        state, _ = State.objects.get_or_create(name=row[8])
        iso, _ = Iso.objects.get_or_create(name=row[10])
        region, _ = Region.objects.get_or_create(name=row[9])
        try:
            year = int(row[3])
        except Exception:
            year = None
        try:
            long = float(row[4])
        except Exception:
            long = None
        try:
            lat = float(row[5])
        except Exception:
            lat = None
        try:
            area_hectares = float(row[6])
        except Exception:
            area_hectares = None

        name = row[0]
        description = row[1]
        justification = row[2]

        site = Site(name=name, description=description, justification=justification,
                    year=year, longitude=long, latitude=lat, area_hectares=area_hectares,
                    category=cat, state=state, region=region, iso=iso)
        site.save()
