# Lists

filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.split()
    for word in words:
        if word in lst:
            continue
        if word not in lst:
        	lst.append(word)
print(sorted(lst))            
            
        