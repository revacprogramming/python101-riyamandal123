# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate:")
r=float(rate)

if h>40:
    
    x=h*r
    y=(h-40)*(r*0.5)
    pay=float(x)+float(y)
    print(pay)

