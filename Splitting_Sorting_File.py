fname = input("Enter file name: ")
fh = open(fname)
line = fh.read()
lst = line.split()
lst.sort()    
print(lst)
	
