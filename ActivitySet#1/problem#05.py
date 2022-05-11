# Functions
def computepay(h, r):
    if h>40:
        x=(40*r)+(h-40)*(1.5*r)
        return x
    else:
        pay=h*r
#print("returning",pay)    
	return pay

hrs = input("Enter Hours:")
h=float(hrs)
rate=input("Enter Rate:")
r=float(rate)    
  
b=computepay(h,r)
print("Pay",b)

    
    
