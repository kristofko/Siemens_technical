# Author : Kristof Siska
# Last edited : Jan 2023

import sys

def check_pal(base) -> bool:
    """check_pal(base) -> bool

    Function to check whether a given argument is a palindrome
    base -- The value to be examined
    """
    if (type(base) != str):
        print(f"{base} is not a string")
        return False

    if (base):
        # Reversing the string 
        rev = base[::-1]
        if rev == base:
            print(f"{base} is a palindrome")
            return True

        print(f"{base} is not a palindrome")
        return False
    
    print("No string to check was given")
    return False

if __name__ == "__main__":
    # We are expecting the argument at the second position
    # The argv list members are always strings, but we can also
    # pass other values and it wont fail.
    check_pal(sys.argv[1])