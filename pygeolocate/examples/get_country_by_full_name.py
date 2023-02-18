import pylocate

united_kingdom = pylocate.locate_by_name("united kingdom")

print(country)
print(country.name)
print(country.coordinates)
print(country.coordinates[0])
print(country.coordinates['long'])