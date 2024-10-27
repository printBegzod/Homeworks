s=str(input('Enter the sentence:'))
a=s.split()
print(a)
for i in range (0,len(a)):
    s=s.replace(a [i],a [i].capitalize())
    print(s)
print(s)
print('BUgUn' in s)