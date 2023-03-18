#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    convert roman numeral to integer
    """
    if not roman_string or roman_string != str:
        return 0
    else:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for letter in roman_string:
            if result < roman[letter] * 5:
                result = result + roman[letter]
            else:
                result = result - roman[letter]
        return result
