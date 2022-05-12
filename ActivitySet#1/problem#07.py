# Strings

text = "X-DSPAM-Confidence:    0.8475"
y=text.find(':')
#print(y)
x=text[y+1:]
#print(x)
z=float(x)
print(z)