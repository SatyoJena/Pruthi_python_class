#strings

s = "abcdefgh"
# len gives length of string
t = "ijkl"

u = s+t 
#concatenates two strings together

v = s*3
#concatenates a string to itself
#multiple times

x = 2   +  3   #5
y = '2' + '3'  #23
print(x,y)

# escape sequences
# \ + some_charcter  = escape sequence
# but how to get \ itself?
# add \ to \ 
print("1. ", "abcd\nefgh") #newline
print("2. ", "abcd\tefgh") #tab
print("3. ", "abcd\refgh") #carriage return
print("4. ", "abcd\fefgh") #line feed
print("5. ", "abcd\\efgh") #escape the slash itself

