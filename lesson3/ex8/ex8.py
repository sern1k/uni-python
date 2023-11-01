def find_common_elements(seq1, seq2):
    # Konwertuj obie sekwencje na zestawy, aby usunąć duplikaty
    set1 = set(seq1)
    set2 = set(seq2)

    # (a) Lista elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń)
    common_elements = list(set1.intersection(set2))

    # (b) Lista wszystkich elementów z obu sekwencji (bez powtórzeń)
    all_elements = list(set1.union(set2))

    return common_elements, all_elements

sequence1 = [1, 2, 3, 4, 4, 5, 6]
sequence2 = [4, 5, 6, 7, 8, 9]

common_elements, all_elements = find_common_elements(sequence1, sequence2)

print("Wspólne elementy:", common_elements)
print("Wszystkie elementy:", all_elements)
