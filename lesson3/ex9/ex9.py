def sum_of_sequences(sequences):
    result = []
    for sequence in sequences:
        total = sum(sequence)
        result.append(total)
    return result

sequences = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
print(sum_of_sequences(sequences))
