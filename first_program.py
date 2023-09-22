
# Write a program to enter any no. check if its -ve, +ve, or 0.

num = int (input ("Enter the number: "))

# input(String) -> String
# int(String) -> int
print("your number was",num, type(num))

#     negative <-- 0 --> positve

if num > 0:
	print("The number", num,  "is positive")
elif num < 0:
	print("The number", num,  "is negative")
else :
	print("The number entered is 0.")