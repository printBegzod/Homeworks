# 1.Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print(set1.union(set2))

# 2.Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print(set1.intersection(set2))

# 3.Difference of Sets: Given two sets, create a new set with elements from the first set that are not in the second.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print(set1.difference(set2))

# 4.Check Subset: Given two sets, check if one set is a subset of the other.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print((set1.intersection(set2)==set1 or set1.intersection(set2)==set2))

# 5.Check Element: Given a set and an element, check if the element exists in the set.
# set1=eval(input('Enter the set: '))
# el1=eval(input('Enter the element: '))
# if el1 in set1:
#     print('The set has such element')
# else:
#      print('The set doesn\'t have such element')

# 6.Set Length: Determine the number of unique elements in a set.
# set1=eval(input('Enter the set: '))
# print('The length of this set is',len(set1))

# 7.Convert List to Set: Given a list, create a new set that contains only the unique elements from that list.
# list1=eval(input('Enter the list: '))
# print(set(list1))

# 8.Remove Element: Given a set and an element, remove the element if it exists.
# set1=eval(input('Enter the set: '))
# el1=eval(input('Enter the element: '))
# if el1 in set1:
#     set1.remove(el1)
# print(set1)

# 9.Clear Set: Create a new empty set from an existing set.
# set1=eval(input('Enter the set: '))
# set1.clear()
# print(set1)

# 10.Check if Set is Empty: Determine if a set has any elements.
# set1=eval(input('Enter the set: '))
# if bool(set1)==0:
#     print('This set is empty')
# else:
#     print('This set is not empty')

# 11.Symmetric Difference: Given two sets, create a new set that contains elements that are in either set but not in both.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print(set1.symmetric_difference(set2))

# 12.Add Element: Given a set and an element, add the element to the set if it is not already present.
# set1=eval(input('Enter the set: '))
# el1=eval(input('Enter the element: '))
# if el1 not in set1:
#     set1.add(el1)
# print(set1)

# 13.Pop Element: Given a set, remove and return an arbitrary element from the set.
# set1=eval(input('Enter the set: '))
# myset=set(set1)
# myset.pop()
# elr=list(set1.difference(myset))[0]
# print('Removed element is',elr)
# print('The set is',set1)

# 14.Find Maximum: From a given set of numbers, find the maximum element.
# set1=eval(input('Enter the set: '))
# print(max(set1))

# 15.Find Minimum: From a given set of numbers, find the minimum element.
# set1=eval(input('Enter the set: '))
# print(min(set1))

# 16.Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.
# set1=eval(input('Enter the set of numbers: '))
# mylist=list(set1)
# newset=set()
# for i in list(mylist):
#     if i%2==0:
#         newset.add(i)
# print(newset)
 
# 17.Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.
# set1=eval(input('Enter the set of numbers: '))
# mylist=list(set1)
# newset=set()
# for i in list(mylist):
#     if i%2==1:
#         newset.add(i)
# print(newset)

# 18.Create a Set of a Range: Create a set of numbers in a specified range (e.g., from 1 to 10).
# n=int(input('Enter the starting number: '))
# m=int(input('Enter the ending number: '))
# myset=set()
# for i in range(n,m+1):
#     myset.add(i)
# print(myset)

# 19.Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.
# list1=eval(input('Enter the set: '))
# list2=eval(input('Enter the set: '))
# set1=set(list1+list2)
# print(set1)

# 20.Check Disjoint Sets: Given two sets, check if they have no elements in common.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# if bool(set1.intersection(set2))==0:
#     print('This sets have no elements in common')
# print('This sets have elements in common')

# 21.Remove Duplicates from a List: Given a list, create a set from it to remove duplicates, then convert back to a list.
# list1=eval(input('Enter the set: '))
# myset=set(list1)
# print(list(myset))

# 22.Get Unique Elements in Order: Given a list, create a set that contains unique elements while maintaining their first appearance order.
# list1=eval(input('Enter the set: '))
# mylist=[]
# for i in list(list1):
#     if i not in mylist:
#         mylist.append(i)
# print(set(mylist))

# 23.Create Nested Sets: Create a set of sets, where each inner set contains a specified number of unique elements.
# n=int(input('Enter the number of element that inner sets should contain: '))
# mylist=[]
# innerset=set()
# for i in range(1,8):
#     for j in range(i*n,i*(n+1)+1):
#         innerset.add(j)
#     set1=frozenset(innerset)
#     mylist.append(set1) 
#     innerset.clear()
# print(set(mylist))  

# 24.Count Unique Elements: Given a list, determine the count of unique elements using a set.
# list1=eval(input('Enter the set: '))
# myset=set(list1)
# print('This list has',len(myset),'unique elements')

# 25.Generate Random Set: Create a set with a specified number of random integers within a certain range.
# s=int(input('Enter starting number of the numbers range: '))
# e=int(input('Enter ending number of the numbers range: '))
# n=int(input('Enter the specified number of random integers: '))
# myset=set()
# for i in range(s,e+1):
#     myset.add(i)
# m=len(myset)-n
# for j in range(0,m):
#     myset.pop()
# print(myset)



