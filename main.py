import random


def guessing_game():
    # Feel free to add words to the list or pull words from a file (words.txt)
    word_list = ["apple", "peach", "banana", "pear", "orange"]
    word_selected = random.choice(word_list).lower()
    word_blanks = ["_" for _ in word_selected]

    user_guesses = []
    guesses = 0

    while True:
        if "_" not in word_blanks:
            print("\n" * 30)
            print(f"Congrats, you found the word -> {word_selected}")
            print(f"You used {guesses} guesses")
            break

        print(" ".join(word_blanks))
        guessed_character = input("\nTake a guess at what the word is. Use one character at a time: ").lower()

        if guessed_character == "quit":
            print(f"The word was {word_selected}. Thanks for playing!")
            break

        # Validate user input
        if not guessed_character.isalpha():
            print("Please enter a valid alphabetical character")
            continue

        guesses += 1

        if guessed_character in word_selected:
            # Replace blanks with guessed character
            for i, char in enumerate(word_selected):
                if guessed_character == char:
                    word_blanks[i] = guessed_character
        else:
            print(f"{guessed_character} is not in the word")


if __name__ == "__main__":
    guessing_game()
