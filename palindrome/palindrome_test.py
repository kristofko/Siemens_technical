# Author : Kristof Siska
# Last edited : Jan 2023

import palindrome

def test_palindrome():
	assert palindrome.check_pal("racecar")

def test_non_palindrome():
	assert not palindrome.check_pal("asad")

def test_palindrome_none():
	assert not palindrome.check_pal(None)

def test_palindrome_not_string():
	assert not palindrome.check_pal(int(123))
