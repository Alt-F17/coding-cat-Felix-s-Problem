def make_combinations_mutation(letters, numbers):
    '''
    Swaps the positions of letter and number in the output pairs.
    '''
    return [[number, letter] for letter in letters for number in numbers]
