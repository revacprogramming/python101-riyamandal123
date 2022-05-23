# Regular Expressions
# https://www.py4e.com/lessons/regex
name = input("Enter file:")
handle = open(name)
for line in handle:
    line=line.rstrip()
    import re
    line=re.findall(('[0-9]+'),line)
    if len(num)<1:
        continue
    num=int(num)
    line.append(line)
    sum=num
print(sum)
    