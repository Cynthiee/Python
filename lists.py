'''
Lists are used to store multiple items in a single variable.
List items are ordered, changeable, and allow duplicate values.
List items are indexed and nested.Index always starts with 0.
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
alist = [90, 'zobo', 29, 'vum', 90]

#append() - appends object to the list.
alist.append('grit')
print("Updated list: ", alist)

#count() - returns the count of how many times object occurs in list.
print("Count for 90: ", alist.count(90))
print("Count for zobo: ", alist.count('zobo'))

#extend() - this method does not return any value but add the content to existing list
blist =['April', 'fool']
alist.extend(blist)
print("Extended list: ", alist)

#index() - returns the index of the found object.
#Otherwise raise an exception indicating value not found.
print("Index for April: ", alist.index('April'))

#insert() - inserts the given element at the given index.
alist.insert(2, 'babe')
print("Inserted list: ", alist)

#pop() - removes object from the list. if called empty, it removes last object in the list
print("A list: ", alist.pop())
print("B list: ", alist.pop(-1))

#remove() - removes given object from the list
alist.remove('vum')
print("Fresh list: ", alist)
alist.remove('grit')
print("Another fresh list: ", alist)

#.reverse() - reverses the given object from the lsit
alist.reverse()
print("Final list: ", alist)

#sort() - it changes the original list by sorting it in either ascending or descending order.
print("Normal list: ", alist)
alist.sort()
print("Sorted list: ", alist)

#built-in functions
#len()- returns the lenght of a list
#list()- creates a new list (list construct)//converts tupule to list
#max()- returns items from the list with max value
#min()- returns intems from list with min value
#cmp()- compares elements of both lists