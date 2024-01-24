import random
from colorama import init, Fore
import hangmanintro
import wordlist
import stages

# Initialize colorama
init(autoreset=True)

def display_welcome():
    print(hangmanintro.hintro[0])

def display_instructions():
    print(Fore.RESET)
    print("1. Start the game")
    print("2. Instructions")
    print("3. Exit the game")

def restart_game():
    while True:
        print(Fore.CYAN + "\nDo you want to restart the game?")
        print("1. Yes")
        print("2. No")
        choice = input("\nEnter your choice (1 or 2): ")

        if choice == '1' or choice == '2':
            return choice == '1'
        else:
            print(Fore.RED + "Invalid choice. Please enter either 1 or 2.")

def get_user_name():
    while True:
        user_name = input(Fore.CYAN + "\nEnter your name: ")
        if user_name.isalpha():  # Check if the input contains only alphabetic characters
            return user_name
        else:
            print(Fore.RED + "Invalid name. Please enter a valid name with only letters.")

def get_single_letter_input(incorrect_guesses):
    while True:
        user_input = input("\nGuess a letter: ").lower()
        if user_input.isalpha() and len(user_input) == 1:
            if user_input not in incorrect_guesses:
                return user_input
            else:
                print(Fore.RED + f"\nYou already guessed the letter '{user_input}' and it was incorrect. Try a different one.")
        else:
            print(Fore.RED + "\nInvalid input. Please enter a single letter.")

# Display welcome message and get user's name
display_welcome()
user_name = get_user_name()

while True:
    display_instructions()
    choice = input(Fore.CYAN + f"\nHello {user_name}! Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Game setup
        list_length = len(wordlist.word_list)
        random_list_word = random.randint(0, list_length)
        word = wordlist.word_list[random_list_word]
        size_word = len(word)
        hangman_word = [char for char in word]
        hangman_word_blank = ["_" for _ in range(size_word)]
        correct_guesses = {char: 0 for char in set(hangman_word)}
        incorrect_guesses = set()

        print(Fore.YELLOW + "\nLet's start the game, {}! \nBelow is a word which has {} blanks to fill in.\n".format(user_name, hangman_word_blank.count("_")))
        print(hangman_word_blank)

        z = 0
        life = 7

        while z >= 0:
            user_input = get_single_letter_input(incorrect_guesses)

            if user_input in hangman_word:
                if correct_guesses[user_input] < hangman_word.count(user_input):
                    for i, char in enumerate(hangman_word):
                        if char == user_input:
                            hangman_word_blank[i] = user_input
                            correct_guesses[user_input] += 1
                    print(Fore.GREEN + f"\nCorrect guess! '{user_input}' is in the word.")
                    print(hangman_word_blank)

                    if set(hangman_word_blank) == set(hangman_word):
                        print(Fore.GREEN + "\nCongratulations! You've Won")
                        print("The correct word was: {}".format(word))
                        break
                else:
                    print(Fore.YELLOW + f"\nYou already guessed all occurrences of the letter '{user_input}'. Try a different one.")
            else:
                print(Fore.RED + f"\nSorry, '{user_input}' is not in the word. You lose a life.")
                life -= 1
                incorrect_guesses.add(user_input)
                print(Fore.YELLOW + f"Attempts left: {life}")
                print(stages.stages_ascii[life])

                if life == 0:
                    print(Fore.RED + "\nYou lost the game. Better luck next time.")
                    print("\nYour word was", format(word))
                    break
            z += 1

        if restart_game():
            continue
        else:
            print(Fore.YELLOW + "Exiting the game. Goodbye!")
            break

    elif choice == '2':
        print(Fore.CYAN + "\nInstructions:")
        print("This is a Hangman game. You need to guess the word by entering letters.")
        print("You have 7 lives. For each incorrect guess, you lose a life.")
        print("If you lose all your lives, the game ends.")
        print("If you guess the word correctly, you win!")

    elif choice == '3':
        print(Fore.YELLOW + "Exiting the game. Goodbye, {}!".format(user_name))
        break

    else:
        print(Fore.RED + "\nInvalid choice.")
