
def main():
	num1=input("Enter the First number: ")
	num2=input("Enter the Second number: ")
	operator=input("Enter the operation: ")
	if (num1.isdecimal()==False or num2.isdecimal()==False):
		print("Not Valid numbers!")
	elif (operator!='+' and operator!='-' and operator!='*' and operator!='/'):
		print("invalid Operation!")
	else:
		if (operator=='+'):
			print(int(num1)+int(num2))
		elif(operator=='-'):
			print(int(num1)-int(num2))
		elif(operator=='*'):
			print(int(num1)*int(num2))
		else: print(int(num1)/int(num2))
	pass
	



if __name__ == '__main__':
	main()
