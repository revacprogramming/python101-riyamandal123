
def add(a, b):
    c=add(a,b)
    return c


def output(a, b, sum):
    print("sum of a and b is a,b,sum")


def main():
  a = int(input("enter a numbers"))
  b = int(input("enter a numbers"))
  sum = add(a, b)
  output(a, b, sum)


x=input('what is the operation')
if __name__ == '__main__':
    main()
