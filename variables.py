'''
Variable is a special word used to describe something.
It helps you talk about something without having to say 
the same thing over and over again. It is like a container 
that hold data or values that you can use in your code. 
It allows you to store and manipulate data in your program.
To assign a variable, all you need to do is
specify the variable name and assign a value to it.
 
'''

#Integer
a = 29
print(a)

#Floating point
pi = 3.14
print(pi)

#String
c = 'A'
print(c)

#Boolean
q = True
print(q)

#Empty value or null data type
x = None
print(x)

#Assigning multiple values to multiple variables
i, j, k = 12, 13, 14
print(i, j, k)

#Assigning unwanted variable with _
m, n, _ = 25, 4, 95
print(m, n)

#Multiple variable names can be assigned to one object
#be, do, to = 7
#print(be, do, to)

#You can modify object to a variable name
y = z = [7, 8, 9]
y = [3, 4, 2]
print(y)
print(z)

#Nested list is also valid
go = [56, 57, [34, 43, 45], 58, 59]
print(go[2])

#You can also reassign a variable to a different data type
a = 'New object'
print(a)