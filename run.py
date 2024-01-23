import random

from colorama import init, Fore
from hangmanintro import hintro
from wordlist import word_list
import stages

# Initialize colorama
init(autoreset=True)

def display_welcome():
    print(hangmanintro.hintro[0])
    print(Fore.CYAN + "Welcome to Hangman!")