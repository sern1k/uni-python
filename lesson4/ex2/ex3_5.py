def make_ruler(n):
    if n < 1:
        print("Miarka musi mieć co najmniej długość 1.")
        return

    ruler_str = ""
    numbers_str = ""

    for i in range(n + 1):
        numbers_str += str(i)
        if i < 9:
            numbers_str += "    "
        else:
            numbers_str += "   "
        ruler_str += "|...."

    ruler_str = ruler_str[:-4]
    numbers_str = numbers_str[:-1]

    return ruler_str + '\n' + numbers_str

print(make_ruler(12))
