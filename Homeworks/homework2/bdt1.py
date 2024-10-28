u=str(input('Enter username : '))
p=str(input('Enter password : '))
if u=='' and p=='':
    print('Error: Both username and password are required.')
elif u=='':
    print('Error: Username cannot be empty.')
elif p=='':
    print('Error: Password cannot be empty')
else:
    print('Valid input!')
    