# Dictionaries

name = input("Enter file:")
handle = open(name)
counts=dict()
l=list()
for lines in handle:
    word=(lines.strip()).split()
    if len(word)<1 or word[0] != 'From':
        continue
        x=word[1]
        print(x)
        
for word in l:
    counts[word]=counts.get(word,0)+ 1
    
        
bigcount=None
bigword=None
for words,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=words
        bigcount=count
print(bigword,bigcount)        

        
      