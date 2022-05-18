# Files
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh =open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("From:"):
        continue
        y=line.find(':')
        #print(y)
        x=line[y+1:]
        #print(x)
        z=float(x)
        #print(z)
        count=count+1
        total=total+z
average=total/count
print("Average spam confidence:",average)



