def cube_number(value):
	return value * 3

def main():
	
	test_value = int(input("Enter a number to cube: "))
	try:
		print("Result is: {}".format(cube_number(test_value)))
	except:
		print("No number entered!")

if __name__ == '__main__':
	main()