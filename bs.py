def binary_search(list, item):
	low = 0 	
	high = len(list)-1
	while low <= high:
		
		mid = int((low+high)/2)
		guess = list[mid]
		if guess == item:
			return guess
	
		elif guess > item:
			print(high)
			high = mid+1
			print(high)
		else:
			print(low)
			low = mid+1
			print(low)
	return None
		

my_list = range(1,100,2)
print(binary_search(my_list, 33))
