# Author : Kristof Siska
# Last edited : Jan 2023

def foo1(items):
	"""
	Function to remove duplicates from a list
	items -- List of items
	"""
	result = []
	for i in range(len(items)):
		
		flag = False
		for j in range(len(result)):
			if (items[i] == result[j]):
				flag = True
				break
			
		if not flag:
			result.append(items[i])
	print(result)


def remove_duplicates(items):
	"""
	Simplified function for removing duplicates from a list
	items -- List of items
	"""
	res = list(set(items))
	print(res)


if __name__ == "__main__":
	check_list = [1,2,3,4,1,2,2,2,2,"Hello", 5,6,6, 132]
	foo1(check_list)
	remove_duplicates(check_list)
