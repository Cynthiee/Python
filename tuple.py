'''
Tuples are defined ny enclosing the elements in ().
Tuples are collection of data that are ordered, indexe and immutable.
Tuples allow duplicates and can  be nested.
There is no ambiguity when defining tuple.
Tuple is similar to lists, only it is immutable.
To define a singleton tuple, include a trailing comma before the closing parentheses.
'''

#Assignment
t = ('we','err', 'red', 'deer') #this list is packed

#to unpack - assign to a new tuple. 
(s1, s2, s3, s4) = t

#swap 
a = 'foo'
b = 'bar'
#print(a, b)
#a,b = b,a
#print("Swapped: ", a,b)
#swapping by assigning a new variable
temp = a
a = b
b = temp
print(a,b)

#Operations in Tuple is same as in Lists
#length
#Concatenation
#Membership
#Iteration
