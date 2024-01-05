# a python program that accepts a number
# checks if it is perfect
"""
1 -> 5 =5 # output mcq/ fill in the blanks
2 -> 3 =6 # classic trivia
3 -> 2 =6 # output
4 -> 2 =8 # program

# f is a factor of n if (n%f ==0)
"""
# what is a perfect number?
# num == sum of its factors
# 6  -> 1 2 3 ++ = 6 => 6 is a perfect number

num  = int(input("Enter a number gora: "))

# pythonic way
if (num == sum([i for i in range(1,num//2 +1) if(num%i == 0)])):
	print("it is a pefect number")
else:
	print("it is not a pefect number")

# noob pythonic way and also comp sci way
s = 0
for i in range(1,num//2 +1):
	if(num%i == 0):
		s+= i
if (s == num):
	print("it is a pefect number")
else:
	print("it is not a pefect number")