'''
Data type is a classification of data that tells the
computer what type of value is stored in a variable.
It tells the computer how to store and manipulate data.
'''

#String Data Type
'''
String are identified as a contiguous set of characters represented 
in the quotation marks.
Python allows for a single or double pairs of quotation marks. 
Strings are immutable sequence data type, i.e each time one makes any changes
to a string, completely new string object is created.
'''
#Text type
#String
str = 'Hello, World'
print(str)
print(str[0])
print(str[0:5])

#NumbericType
#Integer -> whole numbers(positive or negative) without decimals.
int_num = 10

#Float -> number with decimal
float_num = 23.5

#Complex -> numbers and alphabets
#Complex inludes a number with real and imaginary part.
complex_num = 3.24j

print(int_num)
print(float_num)
print(complex_num)

#List Data Type
#List is a collection of items separated by commas and enclosed in [].
#Items in list can be of different data types.
list = [123, 'aba', 10.2, 'zeh']
list1 = ['I am enough']

print(list)
print(list1 * 2)
print(list + list1)

#Set Data Type
'''
Sets are unordered collection of unique objects. It is enclosed in {} and separated by comma.
There are two types of set:
1. Set -> Mutable and new elements can be added once set is defined
2. Frozenset -> Immutable (cannot be changed)
'''

#Set
basket = {'orange', 'apple', 'banana', 'pawpaw', 'apple'}
print(basket) #Duplicated string was removed
a = set('abracadabra')
print(a)
a.add('z') #adds 'z' to the string
print(a)

#Frozenset
b = frozenset('asdfagsa')
print(b)
cities = frozenset({"Frankfurt", "Basel","Freiburg"})
print(cities)

#Dictionary Data Type
#This consists of key-value pairs enclosed in {}.
#Values can be assigned and accessed using [].
dict = {'name':'red', 'age': 10}
print(dict)
print(dict['name'])
print(dict.values())
print(dict.keys())

#Tuple Data Type
#Tuples are immutable and are enclosed in (). 

tuple = (123, 'Hello')
tuple1 = ('world')
print(tuple)
print(tuple[0])
#print(tuple + tuple1)

'''
Python Collections (Arrays)
There are four collection data types in Python
-List is a collection which is ordered and changeable. Allows duplicate members.
-Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-Set is a collection which is unordered, unchangeable, and unindexed. No dupliate members
-Dictionary is a collection which is ordered and changeable. No duplicate members.
'''