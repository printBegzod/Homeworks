
a,b=float(input("x_1=")),float(input("y_1="))
c,d=float(input("x_2=")),float(input("y_2="))
e,f=float(input("x_3=")),float(input("y_3="))
AB=((a-c)**2+(b-d)**2)**(1/2)
BC=((a-e)**2+(b-f)**2)**(1/2)
AC=((e-c)**2+(f-d)**2)**(1/2)
P=AB+BC+AC
p=P/2
S=(p*(p-AB)*(p-AC)*(p-BC))**(1/2)
print("Uchburchakning yuzasi",S,"ga teng")
print('Uchburchakning perimetri',P,'ga teng')
