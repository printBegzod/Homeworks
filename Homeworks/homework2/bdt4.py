a=float(input('Enter the first number : '))
b=float(input('Enter the second number : '))
c=float(input('Enter the third number : '))
x=str(bool(a==b or b==c or a==c))
x=x.replace('True','These 3 numbers are not different')
x=x.replace('False','These 3 numbers are different')
print(x)

