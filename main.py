import random

# Feel Free to add your own words or even a separate file to pull words from
word_list = ["apple", "peach", "banana", "pear", "orange"]
word_selected = random.choice(word_list)
word_blanks = ["_" for i in word_selected]

user_guesses = []
guesses = 0

while True:
    if "_" not in word_blanks:
        print("\n" * 30)
        print(f"Congrats, you found the word -> {word_selected}")
        print(f"You used {guesses} guesses")
        break

    print(word_blanks)
    guessed_character = input("\nTake a guess at what the word is. Use one character at a time: ").lower()
    if guessed_character == "quit":
        break

    # making sure input is at least a character
    if len(guessed_character) != 0:
        guesses += 1

        if guessed_character in [i for i in word_selected]:

            # looping through all words in word_list
            for char in word_selected:
                # lopping through all characters in word from word_list
                if guessed_character == char:
                    # Grabbing the index(es) of the character guess in the word_selected
                    char_enum = [index for (index, item) in enumerate(word_selected) if item == guessed_character]

                    # Iterating through char_enum index(es) within word_selected and replacing blank with guessed char
                    for i in char_enum:
                        word_blanks[i] = guessed_character
        else:
            print(f"{guessed_character} is not in word")

    else:
        print("Please enter a character")
