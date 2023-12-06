#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    else:
        result, i = 0, 0
        num = {
            "CM": 900,
            "CD": 400,
            "M": 1000,
            "D": 500,
            "XC": 90,
            "XL": 40,
            "C": 100,
            "L": 50,
            "IX": 9,
            "IV": 4,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        while i < len(roman_string):
            if i + 1 < len(roman_string) and roman_string[i : i + 2] in num:
                result += num[roman_string[i : i + 2]]
                i += 2
            else:
                result += num[roman_string[i]]
                i += 1
        return result
