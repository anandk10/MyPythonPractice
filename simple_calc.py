def add(a,b):
	"This function adds two numbers and returns the addition"
	print("Adding ",a," and ",b)
	return a+b
	
def sub(a,b):
	"This funtions subtracts the value b from value a and returns the subtraction"
	print("Subtraction ",b,"from ",a)
	return a-b
	
def mul(a,b):
	"This function multiplies value a and value b and returns the multiplication"
	print("Multiplying ",a," and ",b)	
	return a*b

def div(a,b):
	"This function divides value a by value b and returns the division"
	if(b==0):
		return "ERROR: Divide by 0. The divisor cannot be 0."
	print("Dividing ",a," by ",b)
	return a/b
# getting input from the user and calling the functions

print("Enter a : ")
a = int(input())
print("Enter b : ")
b = int(input())

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
input()
	
	