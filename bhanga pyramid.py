# the C fatigue way
n = int(input("Enter N: "))
for i in range(1,n+1) :
	for j in range(1,i+1):
		print("*", end=" ")
	print()

""" the pythonic way
n = int(input("Enter N: "))
for i in range(1,n+1):
	print(" *"*i)
"""
