#    indentation is very important in python
'''
this is
a very big comment
ok?
This is called a multiline comment.
'''

#variables type
#to know type of a variable - use `type` function

a = "Hello world"	 #a is a variable
b = 5
c = 5.0
d = '5.0'
e = "5.0"
f = '''this is a variable'''
print("type of a is" ,type(a))
print("type of b is" ,type(b))
print("type of c is" ,type(c))
print("type of d is" ,type(d))
print("type of e is" ,type(e))
print("type of f is" ,type(f))

#print function

print(a,b)
print(a,b, sep="",end = "")
print(a,b, sep="")
print("this is another print satement")

print(a,b,c,d,e,f, sep=" var ")
print(a," var ",b," var ",c," var ",d," var ",e," var ",f)

print(a,b,c,d,e,f,sep=" var ", end="nothing\n")
sep = " var "
end = "nothing\n"
print(a,sep,b,sep,c,sep,d,sep,e,sep,f,end,sep='')
"""
It prints the value of a variable.
print(a) -> prints the value of `a`

print(a,b) -> prints value of `a` then `b`, separated by space

print options/parameter:
	sep - sets the string of separation between variables
	default value is " " (single space)
	e.g. print(a,b, sep=" "*4)

	end - sets what should be at the end of string it prints
	default value is "\n"(newline )
	e.g. print(a,b, end ="line end lol\n")
"""