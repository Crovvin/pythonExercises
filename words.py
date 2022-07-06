def print_upper_words(words, startingLetter):
    for word in words:
        for letter in startingLetter:
            if word.startswith(letter):
                print(word.upper())