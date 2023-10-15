def count_zeros_in_large_number(number):
    number_str = str(number)

    count = number_str.count("0")

    return count

large_number = 102030405060700
print(f"The number of zeros in the number {large_number} is: {count_zeros_in_large_number(large_number)}")
