import unittest
from conversions_refactored import convert, ConversionNotPossible


class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        test_cases = [
            ("Celsius", "Kelvin", 0.0, 273.15),
            ("Celsius", "Fahrenheit", 100.0, 212.0),

            ("Fahrenheit", "Celsius", 32.0, 0.0),
            ("Fahrenheit", "Kelvin", 212.0, 373.15),

            ("Kelvin", "Celsius", 273.15, 0.0),
            ("Kelvin", "Fahrenheit", 273.15, 32.0)
        ]


        for from_unit, to_unit, value, expected in test_cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit):
                print("Testing", from_unit, "to", to_unit)
                self.assertAlmostEqual(convert(from_unit, to_unit, value), expected)



    def test_distance_conversions(self):
        test_cases = [
            ("Miles", "Yards", 1.0, 1760.0),
            ("Yards", "Miles", 1760.0, 1.0),
            ("Miles", "Meters", 1.0, 1609.344),
            ("Meters", "Miles", 1609.344, 1.0),
            ("Yards", "Meters", 1.0, 0.9144),
            ("Meters", "Yards", 0.9144, 1.0)
        ]

        for from_unit, to_unit, value, expected in test_cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit):
                print("Testing", from_unit, "to", to_unit)
                self.assertAlmostEqual(convert(from_unit, to_unit, value), expected)

    def test_same_unit(self):
        test_cases = [
            ("Celsius", 25.0),
            ("Fahrenheit", 77.0),
            ("Kelvin", 273.15),
            ("Miles", 5.0),
            ("Yards", 10.0),
            ("Meters", 100.0)
        ]

        for unit, value in test_cases:
            with self.subTest(unit=unit):
                print("Testing", unit, "to", unit)
                self.assertAlmostEqual(convert(unit, unit, value), value)


    def test_invalid_conversion(self):
        test_cases = [
            ("Celsius", "Miles", 25.0),
            ("Meters", "Kelvin", 100.0),
            ("Fahrenheit", "Yards", 77.0)
        ]


        for from_unit, to_unit, value in test_cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit):
                print("Testing invalid conversion", from_unit, "to", to_unit)
                with self.assertRaises(ConversionNotPossible):
                    convert(from_unit, to_unit, value)


if __name__ == "__main__":
    unittest.main()