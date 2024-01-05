# a program that accepts a string and checks if
# it is a palindrome 

# what is a palindrome?
# all letters of a word occurs the same backwards
# e.g 
# killik    
# dog god pal sire rise lap dog god

string = input("Enter the string nigga: ")

# pythonic way
if (string == string[::-1]) :
	print("it is a palindrome.")
else :
	print("it is not a palindrome")

# computer science way
n = len(string)
is_palindrome = True
for i in range(0, n//2):
	if(string[i] != string[n-i-1]) :
		print("it is not a palindrome")
		is_palindrome = False

if (is_palindrome):
	print("it is a palindrome.")

