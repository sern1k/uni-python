roman_symbols = 'IVXLCDM'
arabic_values = [1, 5, 10, 50, 100, 500, 1000]

def roman2int(roman):
    result = 0
    prev_value = 0
    for symbol in reversed(roman):
        value = arabic_values[roman_symbols.index(symbol)]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

print(roman2int('MMMDCCXXIV'))
