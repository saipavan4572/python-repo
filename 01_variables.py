# This is single line comment

"""
these 3 double quotes used for multiline comments
"""
a = 68  # this is integer variable
print(a)

# Float value
b = 42.345
print(b)

# Boolean
c = True # true
print(c)

# Strings
d = 'This is a string'
e = "This is also a string"
f = """
    This is a multi line string
    """

# Today's weather is nice
# d = 'I'm learning Python'   # it will throw an error:: SyntaxError: unterminated string literal
# print(d)


d = 'I\'m learning Python'  # this is escape sequence to skip the ' in the string
print(d)

d = "Today's weather is nice"   # this is another way to use ' in the string.
print(d)

# This is a list
test_list = ["hello", "world", "python"]
print(test_list)

# Tuple
test_tuple = ("hello", "world", "python")
print(test_tuple)

# Dict
test_dict = {'a': 1, 'b': 2}
print(test_dict)

# Set
# consider the values in an arbitrary way(unordered)
test_set = {'a', 'b', "abc"}
print(test_set)             # values will not be printed in the order they inserted.


### type() function -> prints the datatype of the variable

print(type(test_dict))
print(type(print))

### Operations ###
# Add
# Sub
# Multi
# Divide
# Integer division
# Modulo division

# Add
a = 42
b = 45.32
c = a + b
print(c)

d = a - b
print(d)

e = a * b
print(e)

#division
f = 12
g = 3
h = f / g   # here it returns float value
print(h, type(h))

# Integer division
h = f // g
print(h, type(h))   # here it returns int value

# Modulo division
i = f % g
print(i)

# Concatenation
a = "42"
b = "43"
print(a + b) # Concatenation

# Power
a = 2
print(a**2) # a²
print(a**3) # a³ 
## superscript:: 10⁴  subscript:: 10₂ 
## In VsCode download the extension "Fast Unicode Math Characters" to type the superscript/subscript
## The hotkeys for ₂ (subscript) is: \_2     #after-typing-the-characters-press-spacebar-or-tab
## The hotkeys for ² (superscript)is: \^2

# Comparison operators
a = 10
b = 20
print("a=10 ; b=20")
res = a > b
print("a > b :",res)
res1 = a < b
print("a < b :",res1)
res2 = a != b
print("a != b :",res2)
res3 = a == b
print("a == b :",res3)
print(res, res1, res2, res3)


# Logical operators
# AND, NOT, OR
a = True
b = False

res = a and b
res_1 = a or b
res_2 = not a
res_3 = not b
print(res, res_1, res_2, res_3)

r1= a & b
print(r1)
r2= a | b
print(r2)
#r3= ~a      # bitwise not ~ operator is deprecated
## 01_variables.py:136: DeprecationWarning: Bitwise inversion '~' on bool is deprecated and will be removed in Python 3.16. This returns the bitwise inversion of the underlying int object and is usually not what you expect from negating a bool. Use the 'not' operator for boolean negation or ~int(x) if you really want the bitwise inversion of the underlying int.
#print(r3)
r31= not a
print(r31)
#r4= ~ b     # bitwise not ~ operator is deprecated
#print(r4)
r5= not b
print(r5)

