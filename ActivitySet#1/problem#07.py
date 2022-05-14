# Strings
text = "X-DSPAM-Confidence:	0.8475"
y=text.find(':')
x=text[y+1:]
z=float(x)
print(z)

