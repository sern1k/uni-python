def replace_gvr_with_name(line):
    return line.replace("GvR", "Guido van Rossum")

line = "Witaj GvR, jesteś genialny!"

print(replace_gvr_with_name(line))
