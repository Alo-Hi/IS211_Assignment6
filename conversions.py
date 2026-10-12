def convertCelsiusToKelvin(celsius):
    """Takes in a Celsius temperature and converts it to Kelvin."""
    kelvins = celsius + 273.15
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a Celsius temperature and converts it to Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def convertFahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    kelvins = (fahrenheit - 32) * 5 / 9 + 273.15
    return kelvins


def convertKelvinToCelsius(kelvins):
    celsius = kelvins - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvins):
    fahrenheit = (kelvins - 273.15) * 9 / 5 + 32
    return fahrenheit
