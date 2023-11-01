def word_length(line):
    return sum(len(word) for word in line)

line = "This is an example string"

print("Amount of words in line: " + str(word_length(line)))
