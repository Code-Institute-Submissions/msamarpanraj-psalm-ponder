import random
from colorama import init, Fore
from hangmanintro import hintro
from wordlist import word_list
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
    