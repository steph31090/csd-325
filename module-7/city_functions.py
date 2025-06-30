# Stephanie Ramos
# June 29, 2025
# Module 7.2 Assignment: Test Case

# This program defines a function that formats a city and country name, optionally including population and language.

def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result
    
# Function calls
# City and Country
print(city_country("santiago", "chile"))

# City, Country, and Population
print(city_country("san luis potosi", "mexico", population=5000000))

# City, Country, Population, and Language
print(city_country("toronto", "canada", population=5000000, language="english"))