'''
Lists are used to store multiple items in a single variable.
List items are ordered, changeable, and allow duplicate values.
List items are indexed.Index always starts with 0.
Negative indexing works as well. -1 refers to the last item, -2 refers to the 2nd-last item.
List may be of different types(heterogeneous)
'''
#Creating a list - List is created using [].
list1 = ['gun', 'sun', 'hun']

list2 = ['abc', 34, True, 40, 'male']
print(type(list2)) #defines the object with the data type 'list'

#list constructor is another way one can create a new list
thislist = list(("apple", "mango", "orange"))
print(thislist)

#List indexing - list items are indexed. 
# you can access them by referring to the index number and the slice operator []
# index starts from 0 and goes to length -1.

lists = [0,1,2,3,4,5]
print(lists[4])
#Range of indexes - here, you specify where to start and end the range
print(lists[:])
print(lists[2:5]) #search starts at index 2, ends at index 5(not included)
print(lists[1:])
print(lists[-1])
print(lists[-4:-1])

#To check if items exist use 'in' keyword
mylist = ['good', 'better', 'best']
if 'best' in mylist:
    print("I'm the " 'best')

#Accessing values in lists
#to change the value of a specific item, refer to the index number
molist = ['boo', 'bae', 'babe']
molist[1] = 'baby'
print(molist)

#to change the value of items within a specific range, 
# refer to the range of index numbers in particular
so = ['do', 're', 'mi', 'fa' ]
so[1:3] = ['la', 'ti']
print(so)

#Basic list operations
#List responds to all general sequence operations
#To find the length of a list
data = [30, 40, 50, 60]
info = ['dog', 'gum', 'mot']

print(len(data))

#Concatenation
print("Concatenated: ", data + info)

#Repititon
wear = ['beads']
print("Repeated: ", wear*4)

# Membership/Boolean
print('dog' in info) 

#Iteration
for data in data:
    print(data)
    
#Methods in Lists
#Append items - appends object to the list.
alist = [90, 'zobo', 29, 'vum']
alist.append('grit')
print("Updated list: ", alist)
