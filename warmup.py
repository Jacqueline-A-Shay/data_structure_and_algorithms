# python3

# first assignment, 
# intro to auto grading system

# read problem
# design algorithm
# implement algorithm
# test and debug
# submit program to grading system

# Sum of two digit

def sum_of_digits(first_digit, second_digit):
	if (1<=first_digit<=9) & (1<=second_digit<=9):
		return first_digit + second_digit
if __name__ == '__main__':
	print("provide 2 single digit numbers separated by a space")
	
	a, b = map(int, input().split())
	print(sum_of_digits(a, b))

