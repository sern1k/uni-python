# Define the input string
def add_underscore_between_characters(input):
    result = ""
    for char in input:
        result += char + "_"

    # Remove the trailing underscore (the last character)
    result = result[:-1]
    return result

word = "word"

# Print the result
print(add_underscore_between_characters(word))
