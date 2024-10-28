sentence=str(input('Enter a string : '))
sentence=sentence.lower()
listed_words=sentence.split()
for i in range(0,len(listed_words)):
    listed_words[i]=listed_words[i].capitalize()
tc_sentence=' '.join(listed_words)
print(tc_sentence)