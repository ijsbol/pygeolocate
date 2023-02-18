"""
MIT License
Copyright (c) 2023-present Scrumpy (Isabelle)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import (
    Union,
    Tuple,
    List,
    Dict,
)

from .structures import (
    Country,
    Coordinates,
)


def _get_raw_country_data() -> List[Dict]:
    with open("pylocate/csv-files/countries.csv", "r") as fp:
        raw_csv_data = fp.read()

    return [
        {
            'code':  country_data.split(",")[0],
            'name': country_data.split(",")[3],
            'coordinates': {
                'latitude': country_data.split(",")[1],
                'longitude': country_data.split(",")[2],
            }
        } for country_data in raw_csv_data.split("\n")
    ]

def locate_by_name(country_name: str) -> List[Country]:
    """
        Returns a list of all possible countries that the `country_name` could reference.

        e.g. "United Kingdom" returns 1 entry as there is only one country called that.
        Whereas just "United" would return 3 entries (United Kingdom, United States, United Arab Emirates).
    """

    countries = _get_raw_country_data()

    return [
        Country(
            country['code'], 
            country['name'], 
            Coordinates(
                country['coordinates']['latitude'], 
                country['coordinates']['longitude']
            )
        ) for country in countries if country_name.lower().replace(" ", "") in country['name'].lower().replace(" ", "") 
    ]

def locate_by_code(country_code: str) -> Union[None, Country]:
    """
        Returns `None` if `country_code` is invalid, else it returns a `Country` object.
    """

    countries = _get_raw_country_data()

    for country in countries:
        if country['code'].lower() == country_code.lower():
            return Country(
                country['code'], 
                country['name'], 
                Coordinates(
                    country['coordinates']['latitude'], 
                    country['coordinates']['longitude']
                )
            )

    return None