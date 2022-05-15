# Files
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence: 0.8475"):
        continue
        y=line.find('0:')
        #print(y)
        x=line[y+1:]
        #print(x)
        z=float(x)
        print(z)
        count=count+1
        total=total+z
average=total/count
print("Average spam confidence:",average)



