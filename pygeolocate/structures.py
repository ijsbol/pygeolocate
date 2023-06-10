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

from typing import Tuple, Union, overload

class Coordinates:
    def __init__(self, latitude: float, longitude: float) -> None:
        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @overload
    def __getitem__(self, item: int) -> float: ...

    @overload
    def __getitem__(self, item: str) -> float: ...

    def __getitem__(self, item: Union[int, str]) -> float:
        if not isinstance(item, (int, str)):  # type: ignore
            raise TypeError("Index must be either an int or a str.")

        if isinstance(item, int):
            if item == 0:
                return self._latitude
            elif item == 1:
                return self._longitude
            else:
                raise IndexError("Index out of range, needs to be either 0 or 1.")

        if item.lower() in ["lat", "latitude"]:
            return self._latitude
        elif item.lower() in ["long", "longitude"]:
            return self._longitude
        else:
            raise ValueError("Item not found.")

    def __tuple__(self) -> Tuple[float, float]:
        return (self._latitude, self._longitude)

    def __str__(self) -> str:
        return f"{self._latitude}, {self._longitude}"

class Country:
    def __init__(self, country_code: str, country_name: str, coordinates: Coordinates) -> None:
        self._country_code = country_code
        self._country_name = country_name
        self._coordinates = coordinates

    @property
    def coordinates(self) -> Coordinates:
        return self._coordinates

    @property
    def name(self) -> str:
        return self._country_name

    @property
    def code(self) -> str:
        return self._country_code

    def __str__(self) -> str:
        return f"{self._country_code} : {self._country_name}"
