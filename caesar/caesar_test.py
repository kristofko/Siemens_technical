# Author : Kristof Siska
# Last edited : Jan 2023

import caesar

def test_encryption_valid_string():
	assert caesar.caesar_encrypt("abcde", 1) == "bcdef" 

def test_encryption_invalid_string():
	assert caesar.caesar_encrypt("1234", 5) == False
