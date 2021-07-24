import random
import constants
from easy_words import word_list

# import random word package
from random_word import RandomWords
r = RandomWords()


# grabs a random word to begin the game with
# if player chooses a long word
def get_hard_word():
    word = r.get_random_word(minLength=8, maxLength=10)
    return word.upper()


def get_easy_word():
    word = random.choice(word_list)
    return word.upper()


# sets state of play and displays the blank spaces for the player to guess
def play(word):
    word_completed = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    incorrect_guesses = 0
    print(display_hangman(incorrect_guesses))
    print(word_completed)
    print("\n")
    # Algorithm below that checks the players input and checks if its right,
    # decrements tries if its wrong and reveals correct guesses. The while
    # loop closes as soon as guessed = True
    while not guessed and incorrect_guesses < 7:
        try:
            guess = input("Please guess a letter or the full word: ").upper()
        except EOFError:
            print("You didn't enter anything, please guess a letter or a word")
        # code runs if player guesses one letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter " + guess)
            elif guess not in word:
                print(guess + " is not in the word.")
                incorrect_guesses += 1
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
                incorrect_guesses += 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completed = word
        else:
            print("Not a valid guess.")
        print(display_hangman(incorrect_guesses))
        print(word_completed)
        print('\n')
        print("You have guessed: " + ', '.join(guessed_letters))
        print("\n")
    if guessed:
        print("Congratulations, you guessed right!")
    else:
        print("Sorry, you ran out of tries. " + "The word was " + word + ".")


def display_hangman(incorrect_guesses):
    constants.hangman_stages
    return constants.hangman_stages[incorrect_guesses]


def main():
    # word = get_word()
    print(constants.lets_play_hangman)
    try:
        easy_or_hard = input("Easy Mode or Hard Mode? (E/H)").upper()
    except EOFError:
        print("You didn't enter anything, please enter E or H.")
    if easy_or_hard == constants.hard_choice:
        word = get_hard_word()
    elif easy_or_hard == constants.easy_choice:
        word = get_easy_word()
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
