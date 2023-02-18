import pylocate

for country in pylocate.locate_by_name("united"):
    print(country)
    print(country.name)
    print(country.coordinates)
    print(country.coordinates[0])
    print(country.coordinates['long'])