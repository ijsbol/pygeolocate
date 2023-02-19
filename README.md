# pygeolocate
 
`pip install -U pygeolocate` or `python -m pip install -U pygeolocate`

<p>
  <img align="center" src="https://img.shields.io/pypi/dm/pygeolocate?style=for-the-badge"/>
  <img align="center" src="https://img.shields.io/github/license/scrumpyy/pygeolocate?style=for-the-badge"/>
  <img align="center" src="https://img.shields.io/github/issues/scrumpyy/pygeolocate?style=for-the-badge"/>
  <br>
  <img align="center" src="https://img.shields.io/github/stars/scrumpyy/pygeolocate?style=for-the-badge"/>
  <img align="center" src="https://img.shields.io/pypi/v/pygeolocate?style=for-the-badge"/>
  <img align="center" src="https://img.shields.io/pypi/pyversions/pygeolocate?style=for-the-badge"/>
</p>

## What is pygeolocate?
Pygeolocate is a simple Python module that allows for developers to get the longitude and latitude coordinates of the geographical center of a country based on Googles dataset.

Pygeolocate also allows for developers to serach countries based on their country code (and vice versa) as well as search for partial country names.

## Get a country by its full name
```python
# pygeolocate/examples/get_country_by_full_name.py
import pygeolocate

united_kingdom = pygeolocate.locate_by_name("united kingdom")[0]

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
