#conditions 
'''
outline
if else < > == != ! not and or
'''

if 2>3 and 3>2 or 55-22 == 33:
	print("I am happy")

else:
	print("I am sed")
#if else clause

'''
grades 
       90 80 70 60 50 33 0
       O  E  A  B  C  D  F
'''
marks = 55

if marks>90 :
	grade = "O"
else :
	if marks>80:
		grade = "E"
	else:
		if marks>70:
			grade = "A"
		else :
			if marks>60:
				grade = "B"
			else :
				if marks>50:
					grade = "C"
				else:
					if marks>33:
						grade = "D"
					else:
						grade = "F"

#if else if else clause
print("grade for marks", marks, "is", grade)

if marks>90 :
	grade = "O"
elif marks>80 :
	grade = "E"
elif marks>70 :
	grade = "A"
elif marks>60 :
	grade = "B"
elif marks>50 :
	grade = "C"
elif marks>33 :
	grade = "D"
else :
	grade = "F"
#if elif else clause
print("grade for marks", marks, "is", grade)


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












