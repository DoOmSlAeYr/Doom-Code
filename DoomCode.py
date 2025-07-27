import os
import sys
import time
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.',
    ')': '-.--.-', '(': '-.--.', ':': '---...',
    ',': '--..--', '=': '-...-', '!': '-.-.--',
    '.': '.-.-.-', '-': '-....-', '+': '.-.-.',
    '"': '.-..-.', '?': '..--..', '/': '-..-.',
    ' ': '/'
}

INVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def clear_screen():
    os.system('clear')

def print_banner():
    banner = pyfiglet.figlet_format("DoomCode")
    print(Fore.CYAN + banner)

def text_to_morse(text):
    result = []
    ignored_chars = set()
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[char])
        else:
            ignored_chars.add(char)
    return ' '.join(result), ignored_chars

def morse_to_text(morse):
    words = morse.strip().split(' / ')
    decoded_words = []
    ignored_codes = set()
    for word in words:
        letters = word.split()
        decoded_letters = []
        for code in letters:
            if code in INVERSE_MORSE_DICT:
                decoded_letters.append(INVERSE_MORSE_DICT[code])
            else:
                ignored_codes.add(code)
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words), ignored_codes

def main():
    clear_screen()
    print_banner()
    print(Fore.YELLOW + "|•| Options:")
    print(Fore.GREEN + " 1 - Text to Morse")
    print(Fore.GREEN + " 2 - Morse to Text")
    print(Fore.RED + " Type 'quit' or 'exit' to leave")
    print(Fore.MAGENTA + "\nby DoomSlayer\n")

    while True:
        choice = input(Fore.CYAN + "Choose option (1/2): ").strip().lower()
        if choice in ['quit', 'exit']:
            print(Fore.YELLOW + "Exiting... Goodbye!")
            break
        elif choice == '1':
            user_text = input(Fore.CYAN + "Enter text to convert: ").strip()
            if user_text.lower() in ['quit', 'exit']:
                print(Fore.YELLOW + "Exiting... Goodbye!")
                break
            morse_result, ignored = text_to_morse(user_text)
            print(Fore.GREEN + "\nMorse code:")
            print(Fore.WHITE + morse_result)
            if ignored:
                print(Fore.RED + f"Ignored unsupported chars: {', '.join(sorted(ignored))}")
            print()
        elif choice == '2':
            user_morse = input(Fore.CYAN + "Enter morse code to convert (use '.' and '-'): ").strip()
            if user_morse.lower() in ['quit', 'exit']:
                print(Fore.YELLOW + "Exiting... Goodbye!")
                break
            text_result, ignored = morse_to_text(user_morse)
            print(Fore.GREEN + "\nDecoded text:")
            print(Fore.WHITE + text_result)
            if ignored:
                print(Fore.RED + f"Ignored unsupported codes: {', '.join(sorted(ignored))}")
            print()
        else:
            print(Fore.RED + "Invalid choice! Please enter 1, 2, quit or exit.\n")

if __name__ == '__main__':
    main()
