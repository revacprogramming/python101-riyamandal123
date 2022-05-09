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



