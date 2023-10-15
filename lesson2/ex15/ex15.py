def concatenate_numbers(list):
    result = ""
    for number in list:
        result += str(number)
    return result

L = [12, 34, 56, 78]

print(concatenate_numbers(L))
