# Author : Kristof Siska
# Last edited : Jan 2023

import sys

def caesar_encrypt(msg : str, shift : int):
    """
    Function to encrypt the given message using caesar cipher

    msg -- string to be encrypted
    shift -- number of characters shift each character of message
    """
    result = ""
    for i in range(len(msg)):
        char = msg[i]

        if (char.isupper()):
           result += chr((ord(char) + shift - 65) % 26 + 65)

        elif (char.islower()):
           result += chr((ord(char) + shift - 97) % 26 + 97)
           
        else:
            print(f"Error : Only roman letters are allowed to be encrypted {char}")
            return False
            
    # Print the encrypted message
    print(f"{result}")
    return result

def read_stdin():
    """
    Function to read message from stdin
    """
    msg = sys.stdin.read()
    # Remove whitespaces
    msg = msg.strip()

    return msg


if __name__ == '__main__':
    shift = 8
    msg = read_stdin()
    caesar_encrypt(msg, shift)