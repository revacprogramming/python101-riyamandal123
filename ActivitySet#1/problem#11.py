# Tuples

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
handle = open(name)
counts=dict()
for line in handle:
    l=line.strip()
    if line.startswith("From"):
        continue
    l=line.split('5:')
for hours in handle:
    counts[hours]=counts.get(hours,0)+1
    
counts=None
hours=None
l=list()
for count,hours in counts.items():
	h=sorted(hours,count)
print(h)

    
    