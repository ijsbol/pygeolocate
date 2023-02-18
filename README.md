# pylocate
 

## Get a country by its full name
```python
# pylocate/examples/get_country_by_full_name.py
import pylocate

united_kingdom = pylocate.locate_by_name("united kingdom")

print(country)
print(country.name)
print(country.coordinates)
print(country.coordinates[0])
print(country.coordinates['long'])
```

## Get a country by part of its name
```python
# pylocate/examples/get_country_by_partial_name.py

import pylocate

for country in pylocate.locate_by_name("united"):
    print(country)
    print(country.name)
    print(country.coordinates)
    print(country.coordinates[0])
    print(country.coordinates['long'])
```