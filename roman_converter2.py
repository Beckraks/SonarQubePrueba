# roman_converter.py

def int_to_roman(num):
    if num < 1 or num > 1000:
        return None  # Manejo de números fuera del rango

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    for value, numeral in roman_numerals.items():
        while num >= value:
            roman_numeral += numeral
            num -= value

    return roman_numeral

print(int_to_roman(250))
