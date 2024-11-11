# 1.Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# if key1 in dict1.keys():
#     print(dict1[key1])
# else:
#     print('There is no such key in this dictionary')

# 2.Check Key: Given a dictionary and a key, check if the key is present in the dictionary.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# if key1 in dict1.keys():
#     print('This key is present in the dictionary')
# else:
#     print('This key is present in the dictionary')

# 3.Count Keys: Determine the number of keys in the dictionary.
# dict1=eval(input('Enter the dict: '))
# keylist=dict1.keys()
# print(len(keylist))

# 4.Get All Keys: Create a list that contains all the keys in the dictionary.
# dict1=eval(input('Enter the dict: '))
# mylist=[]
# keylist=dict1.keys()
# keylist=list(keylist)
# print(keylist)

# 5.Get All Values: Create a list that contains all the values in the dictionary.
# dict1=eval(input('Enter the dict: '))
# print(dict1.values())

# 6.Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.
# dict1=eval(input('Enter the first dict: '))
# dict2=eval(input('Enter the second dict: '))
# keylist=list(dict2.keys())
# valuelist=list(dict2.values())
# for i in range(len(dict2)):
#     dict1[keylist[i]]=valuelist[i]
# print(dict1)

# 7.Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# keylist=list(dict1.keys())
# valuelist=list(dict1.values())
# mydict=dict()
# if key1 in dict1.keys():
#     keylist.remove(key1)
#     valuelist.remove(dict1[key1])
#     for i in range(len(keylist)):
#         mydict[keylist[i]]=valuelist[i]
#     print(mydict)    
# else: 
#     print('There is no such key')

# 8.Clear Dictionary: Create a new empty dictionary.
# mydict=dict()
# print(mydict)

# 9.Check if Dictionary is Empty: Determine if a dictionary has any elements.
# dict1=eval(input('Enter the dict: '))
# if len(dict1)==0:
#     print('Empty dictionary')
# else:
#     print('Not empty dictionary')

# 10.Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# if key1 in dict1.keys():
#     print(key1,':',dict1[key1])
# else:
#     print('There is no such key')

# 11.Update Value: Given a dictionary, update the value for a specified key.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# nv=eval(input('Enter new value: '))
# dict1[key1]=nv
# print(dict1)

# 12.Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.
# dict1=eval(input('Enter the dict: '))
# v1=eval(input('Enter the value: '))
# mylist=list(dict1.values())
# print('This value has',mylist.count(v1),'appearences in the given dictionary')

# 13.Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
# dict1=eval(input('Enter the dict: '))
# mylist1=list(dict1.keys())
# mylist2=list(dict1.values())
# x=0
# clist=mylist2.copy()
# mylist=list()
# mydict=dict()
# for i in range(len(mylist2)):
#     if mylist2.count(mylist2[i])==1:
#         mydict[mylist2[i]]=mylist1[i]
#     else:
#         for j in range(0,(mylist2.count(mylist2[i])-1)):
#             mylist.append(mylist1[(clist.index(mylist2[i])+x)])
#             x+=1
#             clist.remove(mylist2[i])
#         mydict[mylist2[i]]=list(mylist)
# print(mydict)


# 14.Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value
# dict1=eval(input('Enter the dict: '))
# v=eval(input('Enter the value: '))
# l1=list(dict1.keys())
# l2=list(dict1.values())
# mylist=list()
# x=0
# for i in range(0,l2.count(v)):
#     mylist.append(l1[l2.index(v)+x])
#     l2.remove(v)
#     x+=1
# print(mylist)

# 15.Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# l1=eval(input('Enter the list of keys: '))
# l2=eval(input('enter the list of values: '))
# mydict=dict()
# for i in range(len(l1)):
#     mydict[l1[i]]=l2[i]
# print(mydict)

# 16.Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.
# dict1=eval(input('Enter the dict: '))
# l1=list(dict1.values())
# n=0
# for i in list(l1):
#     n+=bool(type(i)==dict)
# print(bool(n))

# 17.Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# dict1=eval(input('Enter the nested dict: '))
# glist=eval(input('Enter a sequence of keys that describes the path to the target value as list: '))
# for i in list(glist):
#     dict1=dict1[i]
# print(dict1)

# 18.Create Default Dictionary: Create a dictionary that provides a default value for missing keys.
# i don't understand this problem

# 19.Count Unique Values: Given a dictionary, determine the number of unique values it contains.
# dict1=eval(input('Enter the dict: '))
# print('This dictionary has',len(set(dict1.values())),'unnique values')

# 20.Sort Dictionary by Key: Create a new dictionary sorted by keys.
# dict1=eval(input('Enter the dict: '))
# mydict=dict1.copy()
# mylist=list(dict1.keys())
# dict1.clear()
# mylist=sorted(mylist)
# for i in list(mylist):
#     dict1[i]=mydict[i]
# print(dict1)

# 21.Sort Dictionary by Value: Create a new dictionary sorted by values.
# dict1=eval(input('Enter the dict: '))
# mydict=dict1.copy()
# mylist1=list(dict1.values())
# mylist2=list(dict1.keys())
# dict1.clear()
# x=0
# mylist=sorted(mylist1)
# for i in list(mylist):
#     dict1[mylist2[(mylist1.index(i)+x)]]=i
#     if mylist.count(i)>1:
#         mylist.remove(i)
#         x+=1
# print(dict1)

# 22.Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# I don't understand the problem

# 23.Check for Common Keys: Given two dictionaries, check if they have any keys in common.
# dict1=eval(input('Enter the first dict: '))
# dict2=eval(input('Enter the second dict: '))
# set1=set(dict1.keys())
# set2=set(dict2.keys())
# if bool(set1.intersection(set2))==0:
#     print('They don\'t have keys in common')
# else:
#     print('They have keys in common')

# 24.Create Dictionary from Tuple: Given a tuple of key-value pairs, create a dictionary from it.
# tuple1=eval(input('Enter the tuple (enterkey and value pairs in subtuple): '))
# mydict=dict()
# for i in tuple(tuple1):
#     mydict[i[0]]=i[1]
# print(mydict)

# 25.Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
# dict1=eval(input('Enter the dict: '))
# tuple1=(list(dict1.keys())[0],dict1[(list(dict1.keys())[0])])
# print(tuple1)












