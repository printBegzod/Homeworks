a=str(input('Enter a string : '))
b=list(a)
for i in range(0,len(a)):
    b[i]=a[len(a)-1-i]
b=''.join(b)
x=str(a==b)
x=x.replace('True','This word is palindrome')
x=x.replace('False','This word is not palindrome')
print(x)