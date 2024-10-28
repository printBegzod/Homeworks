n=int(input('Enter the integer number: '))
m=int(input('Enter the devisor(without 0) : '))
print('Integer devision is ',n//m)
print('Remainder is ',n%m)
#Second solution:
x,y=divmod(n,m)
print('Integer devision is ',x,'and','Remainder is ',y)