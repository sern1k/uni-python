def build_padded_blocks(list):
    return [str(number).zfill(3) for number in list]

L = [7, 24, 123, 6, 9]

print(build_padded_blocks(L))
