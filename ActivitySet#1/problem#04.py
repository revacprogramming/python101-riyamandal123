# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate:")
r=float(rate)

if h>40:
    
    pay=float(40*r) +float( h-40)*float(1.5*r)
    print(pay)
elif h<=40:
    x=h*r
    print("pay:",x)

#to print the gades of students

score = input("Enter Score: ")

x=float(score)
    
if (x>=0.0 and x<=1.0):
    if (x>= 0.9):
        print('A')
    elif(x>= 0.8):
        print('B')
    elif(x>= 0.7):
        print('C')
    elif(x>= 0.6):
        print('D')
    elif(x< 0.6):
        print('F')
else:
        print("error,please enter within the range of input")

    
