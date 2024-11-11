# 1.Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
# tuple1=eval(input('Enter the tuple: '))
# el1=eval(input('Enter an element: '))
# if el1 in tuple1:
#     print('This element has',tuple1.count(el1),'occurences in the given tuple')
# else:
#     print('This element is not exist in the given tuple')

# 3.Max Element: From a given tuple, determine the largest element.
# tuple1=eval(input('Enter the tuple: '))
# print('The largest element is',max(tuple1),'in this tuple')

# 4.Min Element: From a given tuple, determine the smallest element.
# tuple1=eval(input('Enter the tuple: '))
# print('The smallest element is',min(tuple1),'in this tuple')

# 5.First Element: Access the first element of a tuple, considering what to return if the tuple is empty.
# tuple1=eval(input('Enter the tuple: '))
# if bool(tuple1)==0:
#     print('The list is empty')
# else:
#     print('The first element of this tuple is',tuple1[0])

# 6.Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
# tuple1=eval(input('Enter the tuple: '))
# if bool(tuple1)==0:
#     print('The list is empty')
# else:
#     print('The last element of this list is',tuple1[-1])

# 7.Tuple Length: Determine the number of elements in the tuple.
# tuple1=eval(input('Enter the tuple: '))
# print('The length of given tuple is'),len(tuple1))

# 8.Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
# tuple1=eval(input('Enter the tuple: '))
# print('The first 3 elements of this tuple is',tuple1[0:3])

# 9.Concatenate Tuples: Given two tuples, create a new tuple that combines both.
# tuple1=eval(input('Enter first tuple: '))
# tuple2=eval(input('Enter second tuple: '))
# print(tuple(list(tuple1)+list(tuple2)))

# 10.Check if Tuple is Empty: Determine if a tuple has any elements.
# tuple1=eval(input('Enter the tuple: '))
# if bool(tuple1)==0:
#     print('The tuple is empty')
# else:
#     print('The tuple is not empty')

# 11.Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
# tuple1=eval(input('Enter the tuple: '))
# tuple1=list(tuple1)
# el1=eval(input('Enter the element: '))
# n=tuple1.count(el1)
# myset=set()
# if bool(tuple1)==0:
#     print('The tuple is empty')
# else:
#     for i in range(0,n):
#         myset.add((tuple1.index(el1))+i)
#         tuple1.remove(el1)
# print('The set of indexes is:',myset)

# 12.Find Second Largest: From a given tuple, find the second largest element.
# tuple1=eval(input('Enter the tuple: '))
# set1=set(tuple1)
# set1.remove(max(set1))
# print('The second largest element is',max(set1))

# 13.Find Second Smallest: From a given tuple, find the second smallest element.
# tuple1=eval(input('Enter the tuple: '))
# set1=set(tuple1)
# set1.remove(min(set1))
# print('The second smallest element is',min(set1))

# 14.Create a Single Element Tuple: Create a tuple that contains a single specified element.
# el1=eval(input('Enter the element: '))
# myset=(el1,)
# print(myset)

# 15.Convert List to Tuple: Given a list, create a tuple containing the same elements.
# list1=eval(input('Enter the list: '))
# print(tuple(list1))

# 16.Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
# tuple1=eval(input('Enter the tuple: '))
# mylist=list(tuple1)
# mylist.sort()
# print(tuple1==tuple(mylist))

# 17.Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
# tuple1=eval(input('Enter the tuple: '))
# n=int(input('Enter the starting inedx: '))
# m=int(input('Enter the ending index: '))
# mylist=list(tuple1)
# mytuple=tuple(mylist[n:m+1])
# print('The largest element of this subtuple is',max(mytuple))

# 18.Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
# tuple1=eval(input('Enter the tuple: '))
# n=int(input('Enter the starting inedx: '))
# m=int(input('Enter the ending index: '))
# mylist=list(tuple1)
# mytuple=tuple(mylist[n:m+1])
# print('The smallest element of this subtuple is',min(mytuple))

# 19.Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
# tuple1=eval(input('Enter the tuple: '))
# el1=eval(input('Enter the element: '))
# mylist=list(tuple1)
# mylist.remove(el1)
# print(tuple(mylist))

# 20.Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
# tuple1=eval(input('Enter the tuple: '))
# indextuple=eval(input("Enter the tuple that the indexes of elements which are in common subtuple are in the common subtuple and same order: "))
# list1=[]
# mylist=[]
# for i in range (0,len(indextuple)):
#     for j in range (0,len(indextuple[i])):
#         n=indextuple[i][j]
#         mylist.append(tuple1[n])
#     list1.append(tuple(mylist))
#     mylist.clear()
# print(tuple(list1))

# 21.Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
# tuple1=eval(input('Enter the tuple: '))
# n=int(input('Enter the number of time to repeate'))
# mylist=[]
# for i in tuple(tuple1):
#     for j in range(0,n):
#         mylist.append(i)
# print(tuple(mylist))

# 22.Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
# n=int(input('Enter starting number: '))
# m=int(input('Enter ending number '))
# mylist=[]
# for i in range(n,m+1):
#     mylist.append(i)
# print(tuple(mylist))
# 23.Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
# tuple1=eval(input('Enter the tuple: '))
# mylist=list(tuple1)
# print(tuple(mylist[-1::-1]))

# 24.Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
# tuple1=eval(input('Enter the tuple: '))
# mylist=list(tuple1)
# if mylist[-1::-1]==mylist:
#     print('This tuple is palindrome')
# else:
#     print('This tuple is not palindrome')

# 25.Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
# tuple1=eval(input('Enter the tuple: '))
# mylist=[]
# for i in tuple(tuple1):
#     if tuple1.count(i)==1:
#         mylist.append(i)
# print('The unique elements tuple is',tuple(mylist))

