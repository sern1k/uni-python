roman_to_arabic_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman2int(roman):
    result = 0
    prev_value = 0
    for symbol in reversed(roman):
        value = roman_to_arabic_dict.get(symbol, 0)
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

print(roman2int('MMMDCCXXIV'))
