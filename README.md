# pygeolocate
 

## Get a country by its full name
```python
# pygeolocate/examples/get_country_by_full_name.py
import pygeolocate

united_kingdom = pygeolocate.locate_by_name("united kingdom")

print(country)
print(country.name)
print(country.coordinates)
print(country.coordinates[0])
print(country.coordinates['long'])
```

## Get a country by part of its name
```python
# pygeolocate/examples/get_country_by_partial_name.py

import pygeolocate

for country in pygeolocate.locate_by_name("united"):
    print(country)
    print(country.name)
    print(country.coordinates)
    print(country.coordinates[0])
    print(country.coordinates['long'])
```