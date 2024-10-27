A1=float(input('A1 = ')) #A1x+B1y=C1
B1=float(input('B1 = ')) #A2x+B2y=C2
C1=float(input('C1 = '))
A2=float(input('A2 = '))
B2=float(input('B2 = '))
C2=float(input('C2 = '))
x=(C1*B2-C2*B1)/(A1*B2-A2*B1)
y=(C1*A2-C2*A1)/(B1*A2-B2*A1)
print('x =',x,';','y =',y)
