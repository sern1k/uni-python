def amount_of_words(line):
    words = line.split()
    return len(words)

line = "This is an example string"

print("Amount of words in line: " + str(amount_of_words(line)))
