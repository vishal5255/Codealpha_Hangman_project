import random
import time

def display_welcome():
    print("\n===== WELCOME TO HANGMAN =====")
    print("I'll think of a word, and you'll try to guess it one letter at a time.")
    print("You have 6 incorrect guesses before the game ends.")
    print("Some letters will be revealed as hints to help you guess!")
    print("Let's begin!\n")
    time.sleep(1)

def get_random_word():
    word_list = [
        "python", "programming", "computer", "algorithm", "developer",
        "keyboard", "internet", "software", "challenge", "function",
        "variable", "string", "integer", "boolean", "dictionary"
    ]
    return random.choice(word_list)

def add_hints(word):
    # Convert word to list of characters
    word_chars = list(word)
    word_length = len(word)
    
    # Determine how many hints to give based on word length
    # For shorter words, reveal fewer letters
    if word_length <= 5:
        num_hints = 1
    elif word_length <= 8:
        num_hints = 2
    else:
        num_hints = 3
    
    # Create a set to hold positions of revealed letters
    hint_positions = set()
    
    # Randomly select positions to reveal
    while len(hint_positions) < num_hints:
        pos = random.randint(0, word_length - 1)
        hint_positions.add(pos)
    
    # Create a set of the hinted letters
    hinted_letters = {word_chars[pos] for pos in hint_positions}
    
    return hinted_letters

def display_game_status(word, guessed_letters, incorrect_guesses):
    # Display the word with guessed and hinted letters revealed
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    print(f"\nWord: {displayed_word}")
    
    # Show guessed letters
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Incorrect guesses remaining: {6 - incorrect_guesses}")

def play_hangman():
    display_welcome()
    
    word = get_random_word()
    
    # Add hint letters
    hint_letters = add_hints(word)
    
    # Initialize guessed letters with the hints
    guessed_letters = set(hint_letters)
    
    print(f"HINT: I've revealed {len(hint_letters)} letter(s) for you: {', '.join(sorted(hint_letters))}")
    
    incorrect_guesses = 0
    max_incorrect = 6
    
    while incorrect_guesses < max_incorrect:
        display_game_status(word, guessed_letters, incorrect_guesses)
        
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed '{guess}' or it was revealed as a hint. Try a different letter.")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            
            all_letters_guessed = all(letter in guessed_letters for letter in word)
            if all_letters_guessed:
                display_game_status(word, guessed_letters, incorrect_guesses)
                print(f"\nCongratulations! You guessed the word: '{word}'")
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            
            if incorrect_guesses >= max_incorrect:
                display_game_status(word, guessed_letters, incorrect_guesses)
                print(f"\nGame over! The word was: '{word}'")
                break
        
        print("\n" + "-" * 40)
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again.startswith('y'):
        play_hangman()
    else:
        print("\nThanks for playing Hangman! Goodbye!")

if __name__ == "__main__":
    play_hangman()
