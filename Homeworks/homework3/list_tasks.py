#task1
# l=input('Enter list ')
# e=input('Enter element ')
# print(l.count(str(e)))

#task2
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# total=sum(numbers)
# print("The sum of the elements is:", total)

# task3
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# print('The largest element is: ',max(numbers))

# task4
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# print('The smallest element is: ',min(numbers)

# task5
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# myelement =input('ENter the element: ')
# if myelement in mylist:
#     print('This element is present in list')
# else:
#      print('This element is not present in list')

# task6
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# if len(mylist)==0:
#     print('This list is empty')
# else:
#     print("The first element of this list is ",mylist[0])


# task7
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# if len(mylist)==0:
#     print('This list is empty')
# else:
#     print("The last element of this list is ",mylist[-1])

# task8
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# print('The new list is ',list(mylist[:3]))

# task9
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# print('The reversed list is ',list(mylist[::-1]))

# task10
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# print('The sorted list is ',list(sorted(mylist)))

# task11
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# print('The new list without duplicates is ',list(set(mylist)))

# task12
# my_list = input("Enter elements of list separated by spaces: ")
# my_list = list(my_list.split())
# my_element=input('Enter the element ')
# k=int(input('Enter the index '))
# my_list.insert(k,my_element)
# print('The new list is',my_list)

# task13
# my_list = input("Enter elements of list separated by spaces: ")
# my_list = list(my_list.split())
# my_element=input('Enter the element ')
# print('The index(first occurence) of given element is ',my_list.index(my_element))

# task14
# my_list = input("Enter elements of list separated by spaces: ")
# my_list = list(my_list.split())
# print(bool(len(my_list)))

# task15
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# N=0
# for i in numbers:
#     N+=((i+1)%2)
# print(N,' of them are even')

# task16
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# N=0
# for i in numbers:
#     N+=((i)%2)
# print(N,' of them are odd')

# task17
# list_1= eval(input("Enter first list: "))
# list_2= eval((input("Enter second list: ")))
# print(list_1+list_2)

# task18
# list1= eval(input("Enter list: "))
# sublist1= eval(input("Enter sublist list: "))
# n=len(sublist1)
# if sublist1[0] in list1:
#     m=list1.index(sublist1[0])
#     list2=list1[m:m+n]
#     print(sublist1==list2)
# else:
#     print('False')

# task19
# list1= eval(input("Enter list: "))
# el1=eval(input('Enter element to replace: '))
# eln=input('Enter new element: ')
# if el1 in list1:
#     n=list1.index(el1)
#     list1.remove(el1)
#     list1.insert(n,eln)
# else:
#     print('Element is not  found in list')
# print(list1)

# task20
# list1= eval(input("Enter list: "))
# m=max(list1)
# n=list1.count(m)
# for i in range(n):
#     list1.remove(m)
# print('The second largest element is: ',max(list1))

# task21
# list1= eval(input("Enter list: "))
# set1=set(list1)
# set1.remove(min(set1))
# print('The second smallest element is: ',min(set1))

# task22
# list1= eval(input("Enter list: "))
# for i in list(list1):
#     if i%2==1:
#         list1.remove(i)
# print('The set of even numbers is ',list1)

# task23
# list1= eval(input("Enter list: "))
# for i in list(list1):
#     if i%2==o:
#         list1.remove(i)
# print('The set of odd numbers is ',list1)

# task24
# list1= eval(input("Enter list: "))
# print('The number of elements is ',len(list(list1)))

# task25
# list1= eval(input("Enter list: "))
# from copy import copy
# list2=list1.copy()
# print('Copy of the given list is :',list2)

# task26 
# list1= eval(input("Enter list: "))
# list1=list(list1)
# n=len(list1)
# if n%2==0:
#     n1=int(n/2)
#     n2=int((n+2)/2)
#     print('Middle elements are ',list1[n1],'and ',list1[n2])
# else:
#     n3=int((n-1)/2)
#     print('Middle element is ',list1[n3])

# task27
# list1= eval(input("Enter list: "))
# a=int(input('Enter the starting index: '))
# b=int(input('Enter the ending index: '))
# print('Maximum element of a specified sublist is ',max(list1[a:b+1]))   

# task28
# list1= eval(input("Enter list: "))
# a=int(input('Enter the starting index: '))
# b=int(input('Enter the ending index: '))
# print('Minimum element of a specified sublist is ',min(list1[a:b+1])) 

# task29
# list1= eval(input("Enter list: "))
# a=int(input('Enter the index of element: '))
# if a>-len(list1) and a<len(list1):
#     list1.remove(list1[a])
#     print(list1)
# else:
#     print('IndexError')

# task30
# list1= eval(input("Enter the list of numbers: "))
# n=0
# for i in range(0,len(list1)-1):
#     n+=bool(list1[i]<=list1[i+1])
# print(n==len(list1)-1)

# task31
# list1= eval(input("Enter the list of numbers: "))
# n=int(input('Enter number: '))
# list2=list1.copy()
# for i in range(0,len(list1)):
#     for j in range(1,n):
#        list2.insert(n*i,list1[i])
# print(list2)

# task32
# list1= eval(input("Enter the first list: "))
# list2= eval(input("Enter the second list: "))
# list_merge=list1+list2
# list_merge.sort()
# print(list_merge)

# task33
# list1= eval(input("Enter the list: "))
# element1=eval(input('Enter the element: '))
# n=list1.count(element1)
# listofindexes=[]
# for i in range(0,n):
#     listofindexes.append(list1.index(element1)+i)
#     list1.remove(element1)
# print('Index list of this element in the given list is: ',listofindexes)

# task34
# list1= eval(input("Enter the list: "))
# n=int(input('Enter the number of positions to shift: '))
# n=n%(len(list1))
# print('The rotated list is: ',list1[-n:]+list1[:-n])

# task35
# n=int(input('Enter starting number: '))
# m=int(input('Enter ending number: '))
# listr=[]
# for i in range(n,m+1):
#     listr.append(i)
# print(listr)

# task36
# list1= eval(input("Enter the list of numbers: "))
# S=0
# for i in list(list1):
#     if i>0:
#         S+=i
# print('The sum of all positive numbers is: ',S)

# task37
# list1= eval(input("Enter the list of numbers: "))
# S=0
# for i in list(list1):
#     if i<0:
#         S+=i
# print('The sum of all negative numbers is: ',S)

# task38
# list1= eval(input("Enter the list of numbers: "))
# checklist=list1[-1::-1]
# if list1==checklist:
#     print('This list is a palindrome')
# else:
#     print('This list is not a palindrome')

# task39
# list1= eval(input("Enter the list of numbers: "))
# n=int(input('Enter the number of elements that every sublists should contain: '))
# newlist=[]
# r=(len(list1))%n
# for i in range(0,(len(list1)-r)//n):
#     newlist.append(list(list1[i*n:(i+1)*n]))
# newlist.append(list(list1[-r:]))
# print('The nested list is ',newlist)

# task40
# list1= eval(input("Enter the list: "))
# newlist=[]
# for i in list(list1):
#     if list1.count(i)==1:
#         newlist.append(i)
# print(newlist)