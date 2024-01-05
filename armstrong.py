# accepts a number. checks if 
# it is an armstrong number

num = int(input("Enter the number nigga: "))
num_copy = num

# pythonic way
if (num == sum([int(i)**3 for i in str(num)])) :
	print("it is armstrong number")
else:
	print("it is not armstrong number")

# computer science way
s = 0
while(num>0) :
	s += (num%10)**3
	num //= 10
if (s == num_copy):
	print("it is armstrong number")
else:
	print("it is not armstrong number")