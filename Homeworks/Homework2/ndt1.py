n=float(input('Enter a number:'))
if n==0:
    print(n)
else:
    an=(n**2)**(1/2)
    intn=(an*1000)//1
    x=intn%10
    k=(x-4.5)/((x-4.5)**2)**(1/2)
    y=(intn-x+5+k*5)/1000
    yn=y*(n/an)
    print(yn)