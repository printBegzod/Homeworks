s=str(input('Enter a sentence:'))
a=s.split()
for i in range (0,len(a)):
    a[i]=a[i].capitalize()
s=' '.join(a)
print(s)