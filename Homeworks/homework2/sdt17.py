sentence=str(input('Enter a sentence : '))
a=sentence.split()
b=list(a)
for i in range(0,len(a)):
    b[i]=a[len(a)-1-i]
sentence=' '.join(b)
print(sentence)