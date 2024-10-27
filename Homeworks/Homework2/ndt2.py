a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
if a>b>c:
    print('the largest one is',a,'and','the smallest one is',c)
elif a>c>b:
    print('the largest one is',a,'and','the smallest one is',b)
elif b>a>c:
    print('the largest one is',b,'and','the smallest one is',c)
elif b>c>a:
    print('the largest one is',b,'and','the smallest one is',a)
elif c>a>b:
    print('the largest one is',c,'and','the smallest one is',b)
else:
    print('the largest one is',c,'and','the smallest one is',a)