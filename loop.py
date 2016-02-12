testing_while = int(input())
testing_for = int(input())

temp = testing_while
temp1 = testing_for
while(temp > 0 or temp1 > 0):
	print("the value of temp is now ",temp)
	if(temp>=0):
		temp = temp-1
	if(temp<0):
		print("temp1 value ",temp1)
		temp1-=1
input()

if(testing_for>testing_while):
	min = testing_while
	max = testing_for
else:
	max = testing_while
	min = testing_for
	

for i in range(min, max+1):
	if((i%2)==0):
		print(i," is a even number.")
	else:
		print(i," is an odd number")
input()
		
