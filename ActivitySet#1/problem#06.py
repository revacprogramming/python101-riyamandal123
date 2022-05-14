# Loops & Iterators
largest = none
smallest = none

while True:
    num = (input("Enter a number: ")
    if num == "done":
       break
    	print(num)
    try:
        x=int(num)
        if lagest is none or largest<x:
            largest=x
        if smallest is none or smallest>x:
            smallest=x
	except:
        print("Invalid input")
        continue
        
   
print("Maximum is",largest)       
print("Minimum is",smallest)
