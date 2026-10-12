class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    temperatures = ["Celsius", "Fahrenheit", "Kelvin"]
    distances = ["Miles", "Yards", "Meters"]

    if fromUnit not in temperatures + distances:
        raise ConversionNotPossible()

    if toUnit not in temperatures + distances:
        raise ConversionNotPossible()

    if fromUnit in temperatures and toUnit in distances:
        raise ConversionNotPossible()

    if fromUnit in distances and toUnit in temperatures:
        raise ConversionNotPossible()

    if fromUnit == toUnit:
        return value

    if fromUnit in temperatures:
        if fromUnit == "Celsius":
            celsius = value
        elif fromUnit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        else:
            celsius = value - 273.15

        if toUnit == "Celsius":
            return celsius
        elif toUnit == "Fahrenheit":
            return celsius * 9 / 5 + 32
        else:
            return celsius + 273.15

    if fromUnit == "Miles":
        meters = value * 1609.344
    elif fromUnit == "Yards":
        meters = value * 0.9144
    else:
        meters = value

    if toUnit == "Miles":
        return meters / 1609.344
    elif toUnit == "Yards":
        return meters / 0.9144
    else:
        return meters