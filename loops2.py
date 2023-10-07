#!/usr/bin/python3
"""
s= '''
*****
 ***
  *
 ***
*****
'''
print(s)
"""



'''
take user input 'n'
print n such lines
*       print('*')     print('*'*1)
**      print('**')    print('*'*2)
***     print('***')   print('*'*3)
****    print('****')  print('*'*4)
......  .....          .... n times
'''

# loop use haba
# range us ehaba
# variable

print("question 1")
n = int(input("enter a number: "))

for i in range(1,n+1):
	print('*'*i)


'''
******
****
***
**
*
'''

print("Question 2")
n = int(input("enter a number: "))

for i in range(n): # 1,2,3 .. n-1
	print('*'*(n-i)) # '*'*4  '*'*3 ...


print("Question 3- do both")
# just combine lol

n = int(input("enter a number: "))

for i in range(n): # 1,2,3 .. n-1
	print('*'*(n-i))
for i in range(1,n+1):
	print('*'*i)

print("Question 4 - with gaps")
# hint: print space or use it as a string multiplier
n= int(input("enter: "))
for i in range(n):
	print(' '*(n-i) + '*'*i)

print("Question 5 - with gaps from both sides")
# hint: use space + star as a string multiplier
n= int(input("enter: "))
for i in range(n):
	print(' '*(n-i) + ' *'*i)
