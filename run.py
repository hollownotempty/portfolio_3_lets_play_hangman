import constants

# import random word package
from random_word import RandomWords
r = RandomWords()


# grabs a random word to begin the game with
# if player chooses a long word
def get_long_word():
    word = r.get_random_word(minLength=8, maxLength=10)
    return word.upper()


def get_short_word():
    word = r.get_random_word(minLength=3, maxLength=6)
    print(word)
    return word.upper()


# sets state of play and displays the blank spaces for the player to guess
def play(word):
    word_completed = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(display_hangman(tries))
    print(word_completed)
    print("\n")
    # Algorithm below that checks the players input and checks if its right,
    # decrements tries if its wrong and reveals correct guesses. The while
    # loop closes as soon as guessed = True
    while not guessed and tries > 0:
        try:
            guess = input("Please guess a letter or word: ").upper()
        except EOFError as e:
            print(e)
        # code runs if player guesses one letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter " + guess)
            elif guess not in word:
                print(guess + " is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Correct, " + guess + " is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completed)
                x = [i for i, letter in enumerate(word) if letter == guess]
                for i in x:
                    word_as_list[i] = guess
                word_completed = "".join(word_as_list)
                if "_" not in word_completed:
                    guessed = True
        # code runs if player guesses the full word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word " + guess)
            elif guess != word:
                print(guess + " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completed = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completed)
        print('\n')
        print("You have guessed: " + ', '.join(guessed_letters))
        print("\n")
    if guessed:
        print("Congratulations, you guessed right!")
    else:
        print("Sorry, you ran out of tries. " + "The word was " + word + ".")


def display_hangman(tries):
    stages = [  # seventh attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # sixth attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # fifth attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # fourth attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # third attempt
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # second attempt
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |
                   |
                   -
                """,
                # first attempt
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # starting state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    # word = get_word()
    print(constants.lets_play_hangman)
    try:
        l_or_s = input("Short word or long word? (L/S)").upper()
    except EOFError as e:
        print(e)
    if l_or_s == "L":
        word = get_long_word()
    elif l_or_s == "S":
        word = get_short_word()
    else:
        print('Not a valid input.')
        main()
    play(word)
    if input("Play Again? (Y/N) ").upper() == "Y":
        main()
    else:
        exit()


if __name__ == "__main__":
    main()
