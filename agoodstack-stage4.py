def create_flashcards(num_cards):
    flashcards = {}
    for i in range(1, num_cards + 1):
        print(f'The term for card #{i}:')
        term = input()

        # Check for duplicate term
        while term in flashcards:
            print(f'The term "{term}" already exists. Try again:')
            term = input()

        print(f'The definition for card #{i}:')
        definition = input()

        # Check for duplicate definition
        while definition in flashcards.values():
            print(f'The definition "{definition}" already exists. Try again:')
            definition = input()

        flashcards[term] = definition
    return flashcards


def get_term_by_definition(flashcards, definition):
    for term, defn in flashcards.items():
        if defn == definition:
            return term
    return None


def test_flashcards(flashcards):
    for term, definition in flashcards.items():
        print(f'Print the definition of "{term}":')
        user_answer = input()

        if user_answer == definition:
            print('Correct!')
        else:
            # Check if user's definition matches another term
            matching_term = get_term_by_definition(flashcards, user_answer)

            if matching_term:
                print(
                    f'Wrong. The right answer is "{definition}", but your definition is correct for "{matching_term}".')
            else:
                print(f'Wrong. The right answer is "{definition}".')


def main():
    print('Input the number of cards:')
    num_cards = int(input())
    flashcards = create_flashcards(num_cards)
    test_flashcards(flashcards)


if __name__ == '__main__':
    main()