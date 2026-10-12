import unittest
from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)


class TestTemperatureConversions(unittest.TestCase):

    def test_celsius_to_kelvin(self):
        test_cases = [
            (0.0, 273.15),
            (100.0, 373.15),
            (-40.0, 233.15),
            (25.0, 298.15),
            (-273.15, 0.0)
        ]

        for celsius, expected in test_cases:
            with self.subTest(celsius=celsius):
                print("Testing", celsius, "Celsius to Kelvin")
                self.assertAlmostEqual(convertCelsiusToKelvin(celsius), expected)

    def test_celsius_to_fahrenheit(self):
        test_cases = [
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (25.0, 77.0),
            (300.0, 572.0)
        ]
        for celsius, expected in test_cases:
            with self.subTest(celsius=celsius):
                print("Testing", celsius, "Celsius to Fahrenheit")
                self.assertAlmostEqual(convertCelsiusToFahrenheit(celsius), expected)

    def test_fahrenheit_to_celsius(self):
        test_cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (77.0, 25.0),
            (98.6, 37.0)
        ]

        for fahrenheit, expected in test_cases:
            with self.subTest(fahrenheit=fahrenheit):
                print("Testing", fahrenheit, "Fahrenheit to Celsius")
                self.assertAlmostEqual(convertFahrenheitToCelsius(fahrenheit), expected)

    def test_fahrenheit_to_kelvin(self):
        test_cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (77.0, 298.15),
            (-459.67, 0.0)
        ]




        for fahrenheit, expected in test_cases:
            with self.subTest(fahrenheit=fahrenheit):
                print("Testing", fahrenheit, "Fahrenheit to Kelvin")
                self.assertAlmostEqual(convertFahrenheitToKelvin(fahrenheit), expected)

    def test_kelvin_to_celsius(self):
        test_cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (233.15, -40.0),
            (298.15, 25.0),
            (0.0, -273.15)
        ]

        for kelvins, expected in test_cases:
            with self.subTest(kelvins=kelvins):
                print("Testing", kelvins, "Kelvin to Celsius")
                self.assertAlmostEqual(convertKelvinToCelsius(kelvins), expected)

    def test_kelvin_to_fahrenheit(self):
        test_cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (233.15, -40.0),
            (298.15, 77.0),
            (0.0, -459.67)
        ]

        for kelvins, expected in test_cases:
            with self.subTest(kelvins=kelvins):
                print("Testing", kelvins, "Kelvin to Fahrenheit")
                self.assertAlmostEqual(convertKelvinToFahrenheit(kelvins), expected)

if __name__ == "__main__":
    unittest.main()