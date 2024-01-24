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