def sort_words_alphabetically(line):
    words = line.split()
    return sorted(words, key=lambda x: x.lower())

def sort_words_by_length(line):
    words = line.split()
    return sorted(words, key=len)

line = "This is an example string to sort"

print("Sorted alphabetically:", sort_words_alphabetically(line))
print("Sorted by length:", sort_words_by_length(line))
