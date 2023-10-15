def count_words_in_string(line):
    lines = line.split('\n')

    counter = 0
    for line in lines:
        words = line.split()
        counter += len(words)

    return counter

line = """
This is
an example
multi-line
string
"""

print("Number of words in the string: ", count_words_in_string(line))
