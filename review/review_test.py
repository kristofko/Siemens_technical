# Author : Kristof Siska
# Last edited : Jan 2023

import review

def test_remove_duplicates_1():
	assert review.remove_duplicates([1,2,3,3,5,1]) == [1,2,3,5]


def test_remove_duplicates_2():
	assert review.remove_duplicates([1,2,2,1,"Hello",1,"Hello", 1,1,2,2,2]) == [1,2,"Hello"]

