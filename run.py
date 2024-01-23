import random
import hangmanintro
import wordlist
import stages
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def display_welcome():
    print(hangmanintro.hintro[0])
    print(Fore.CYAN + "Welcome to Hangman!")