chitha = ["vendi", "alu", "gobi", "piaja"] # creation
print(chitha[0]) # access indices of list
print(chitha[1])
print(chitha[2])
print(chitha[3])
#print(chitha[4]) # error list index out of range

chitha.append("dhania")
print(chitha[4])

print("list before change: ")
print(chitha)

chitha[2] = "phulkobi" # access index to edit it.
print("list after change: ")
print(chitha)
