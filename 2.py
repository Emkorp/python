

l = input("Write the numbers of the list: ").split()
l[:-1:2], l[1::2] = l[1::2], l[:-1:2]
print(l)