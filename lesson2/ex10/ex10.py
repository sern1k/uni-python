def count_words_in_string(string):
    # Divide the string into lines
    lines = string.split('\n')

    counter = 0
    for line in lines:
        words = line.split()
        counter += len(words)

    return counter

# Example multi-line string
string = """
This is
an example
multi-line
string
"""

# Call the function and display the result
print("Number of words in the string: ", count_words_in_string(string))
