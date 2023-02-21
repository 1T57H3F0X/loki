# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
from pathlib import Path
from cryptography.fernet import Fernet

# Pre-run.
#os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Config (Prints).
print_text = (f"{Fore.WHITE}") # Change the colour of text output in the client side prints.
print_dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side prints.
print_success = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]") # Success output.
print_successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]") # Successfully output.
print_failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]") # Failed output.
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]") # Prompt output.
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]") # Notice output.
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]") # Alert output.
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]") # Alert output.
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]") # Execited output.
print_disconnected = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]") # Disconnected output.
print_command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ") # Always asks for a command on a new line.

# Program.
def keygen():
    try:
        print(f"\n{print_question} Do you want to back up your current key? [Y/n]")
        option = input(f"{print_command}")
        key_path = './var/pipes/loki.key'
        option = option.lower()

        # Backup key
        if option == 'y':
            with open(key_path, 'r') as loki_key:
                print(f'\n{print_prompt} Pevious key: {loki_key.read()}')
            os.system(f'cp {key_path} {key_path}.bk')

        # Generate new key
        with open(key_path, 'wb') as loki_key:
            key = Fernet.generate_key()
            loki_key.write(key)
            print(f'\n{print_alert} New key: {key.decode("utf8")}\n')

        if option == 'n':
            print(f'\n{print_exited} {print_notice} {print_successfully}\n')

# Error handling.
    except KeyboardInterrupt:
        print(f"\n{print_exited} {print_notice} {print_successfully}")
        print(f'{print_notice} You interrupted the program.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except ValueError:
        print(f"\n{print_exited} {print_notice} {print_successfully}")
        print(f'{print_notice} You entered invalid data into a field.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)