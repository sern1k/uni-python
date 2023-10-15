def string_from_first_chars(line):
    words = line.split()
    return "".join([word[0] for word in words])

def string_from_last_chars(line):
    words = line.split()
    return "".join([word[-1] for word in words])

line = "This is an example string"

print("String from the first characters of words: ", string_from_first_chars(line))
print("String from the last characters of words: ", string_from_last_chars(line))
