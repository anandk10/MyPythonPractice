# Enter your code here. Read input from STDIN. Print output to STDOUT
# Problem link  : https://www.hackerrank.com/challenges/python-mod-divmod
# Python 2.7
from __future__ import division
num1 = int(raw_input())
num2 = int(raw_input())
print(num1//num2)
print(num1%num2)
print(divmod(num1,num2))