import itertools # Pre-Installed
import string # Pre-Installed
from colorama import Fore,init # pip install colorama
import pyautogui # pip install pyautogui

init() # Don't required for linux

def guess_password(password):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits # a-zA-Z0-9 #string.punctuations
    attempts = 0

    try:
        for pass_len in range(1,len(password)+1):
            for guess in itertools.product(chars,repeat=pass_len):
                attempts += 1
                guess = ''.join(guess)

                if guess == password:
                    print(Fore.RED + f'\n...Congrats! Password is Cracked... after {attempts} Attempts' + Fore.RESET)
                    return f'Cracked Password is : {Fore.GREEN + guess + Fore.RESET}'
                
                print(f'Guessed Password : {Fore.MAGENTA + guess + Fore.RESET} <<<< {attempts} Attempts Done...')
    except KeyboardInterrupt:
        print(Fore.RED + 'Stopped Working...' + Fore.RESET)
        exit()

pwd = pyautogui.password('Enter a Password','Password')
print(guess_password(pwd))