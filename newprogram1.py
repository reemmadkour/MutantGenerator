import sys
b = int(sys.argv[1])
a = b-2	#mutant
b = a-1
c = b/2
d = a*b
arr=list()
arr.append(a)
arr.append(b)
arr.append(c)
arr.append(d)
print(arr)
