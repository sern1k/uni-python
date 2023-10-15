def find_longest_word(line):
    words = line.split()
    if len(words) == 0:
        return None
    longest_word = max(words, key=len)
    return longest_word

line = "This is an example string"

if find_longest_word(line) != None:
    print(f"The longest word is '{find_longest_word(line)}' with a length of {len(find_longest_word(line))} characters.")
else:
    print("The longest word is None with a length of 0 characters.")
