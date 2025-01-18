sample_str = "This is a sample string"
sample_str_list = list(sample_str)      # string to list
print(sample_str_list)

sample_str_tuple = tuple(sample_str)    # string to tuple
print(sample_str_tuple)

# Accept input from a user --> input() can be used.
user_input = input("Enter a number: ")   # by default input data can be treated as string
print(user_input, type(user_input))

#add_10 = user_input + 10
#Error:
""" 
Traceback (most recent call last):
  File "D:\Personal\DevOps\JoinDevOps-SivaKumarReddy\shell-script-repo\python-repo\07_type_casting.py", line 12, in <module>
    add_10 = user_input + 10
             ~~~~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str
"""
# To fix the above error we need to type caste the input datatype to int
add_10 = int(user_input) + 10
print(add_10)

# split the user input
user_input = input("Enter numbers: ") 
split_input = user_input.split(" ")
print(split_input,type(split_input))
"""
Enter numbers: 8 21 17 15 43 39 62
['8', '21', '17', '15', '43', '39', '62'] <class 'list'>
"""
