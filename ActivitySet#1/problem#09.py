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
            
#8.5         
fname = input("Enter file name: ")
fh = open(fname)
l=list()
count = 0
for line in fh:
    x=line.rstrip()
    words=line.split()
    if len(words)<1 or words[0]!='From':
        continue
    print(words[1])    
    count=count+1
print("There were", count, "lines in the file with From as the first word")
