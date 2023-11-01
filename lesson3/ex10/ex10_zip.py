roman_symbols = 'IVXLCDM'
arabic_values = [1, 5, 10, 50, 100, 500, 1000]

roman_to_arabic_dict = dict(zip(roman_symbols, arabic_values))

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
