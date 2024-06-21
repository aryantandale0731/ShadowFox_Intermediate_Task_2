import random

# Predefined list of words
words = ["python", "hangman", "challenge", "programming", "computer", "interface"]

def choose_word():
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 6
    tries = 0

    print("Welcome to Hangman!")

    while tries < max_attempts:
        print(display_hangman(tries))
        print("Word:", display_word(word, guessed_letters))
        print("Incorrect guesses:", ' '.join(sorted(incorrect_guesses)))
        
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses.add(guess)
            tries += 1
        
    else:
        print(display_hangman(tries))
        print(f"Sorry, you lost! The word was: {word}")

def main():
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
