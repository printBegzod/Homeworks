a=str(input('Enter a string : '))
b=list(a)
for i in range(0,len(a)):
    b[i]=a[len(a)-1-i]
b=''.join(b)
print(b)
