# Stephanie Ramos
# June 29, 2025
# Module 7.2 Assignment: Test Case

# The purpose of this code is to test the `city_country` function from the `city_functions` module.

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country("santiago", "chile"), "Santiago, Chile")
        self.assertEqual(city_country("san luis potosi", "mexico"), "San Luis Potosi, Mexico")
        self.assertEqual(city_country("toronto", "canada"), "Toronto, Canada")

if __name__ == '__main__':
    unittest.main()