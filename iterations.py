#iterations
'''
outline
for while range in 
list str
'''
chitha = ["vendi", "alu", "gobi", "piaja"] # creation

for pariba in chitha: # pariba is a temporary variable
	print("pariba is ", pariba)

print("\nfor loop: ")
for i in range(len(chitha)):
	print("pariba at index =", i, "is", chitha[i])


print("\nwhile loop: ")
index = 0
while (index <= 3) : # like if statement
	print("pariba at index =", index, "is", chitha[index])
	index = index + 1
"""
start:
	index = 0 
	if (index < len(chitha)): -> false hele GOTO exit
		pariba  = chitha[index]
		go inside `for` block
		use value of pariba
		index = index + 1
	goto start

exit:
	...
	...
"""