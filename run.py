# import random word package
from random_word import RandomWords
r = RandomWords()


# grab random word to begin the game with
def get_word():
    word = r.get_random_word(minLength=4, maxLength=8)
    return word.upper()


# sets state of play and displays the blank spaces for the player to guess
def play(word):
    word_completed = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("""
        
 _        ___  ______  __   _____     ____   _       ____  __ __      __ __   ____  ____    ____  ___ ___   ____  ____   __ 
| |      /  _]|      ||  | / ___/    |    \ | |     /    ||  |  |    |  |  | /    ||    \  /    ||   |   | /    ||    \ |  |
| |     /  [_ |      ||_ |(   \_     |  o  )| |    |  o  ||  |  |    |  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  ||  |
| |___ |    _]|_|  |_|  \| \__  |    |   _/ | |___ |     ||  ~  |    |  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  ||__|
|     ||   [_   |  |       /  \ |    |  |   |     ||  _  ||___, |    |  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  | __ 
|     ||     |  |  |       \    |    |  |   |     ||  |  ||     |    |  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  ||  |
|_____||_____|  |__|        \___|    |__|   |_____||__|__||____/     |__|__||__|__||__|__||___,_||___|___||__|__||__|__||__|
                                                                                                                            

                """)
    print(display_hangman(tries))
    print(word_completed)
    print("\n")
    # Algorithm below that checks the players input and checks if its right, 
    # decrements tries if its wrong and reveals correct guesses. The while 
    # loop closes as soon as guessed = True
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
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
        print("You have guessed: " + ', '.join(guessed_letters))
        print("\n")
    if guessed:
        print("Congratulations, you guessed right!")
    else:
        print("Sorry, you ran out of tries. " + "The word was " + word + ".")


def display_hangman(tries):
    stages = [  # sixth attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # fifth attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # fourth attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # third attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|
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
                   |      |
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
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
