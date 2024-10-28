email=str(input('Enter your email adress : '))
k=email.find('@')
username=email[:k]
print('Your username is ',username)