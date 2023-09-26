import pylocate

united_kingdom = pylocate.locate_by_name("united kingdom")[0]

print(united_kingdom)
print(united_kingdom.name)
print(united_kingdom.coordinates)
print(united_kingdom.coordinates[0])
print(united_kingdom.coordinates['long'])