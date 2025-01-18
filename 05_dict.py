# dict is a mutable datatype

sample_dict = {1: 1, 2: 4, 3: 9} # dict()
# Keys in dictionary should of immutable datatype
print(sample_dict[3])

sample_dict = {1: 1, 2: 4, 3: 9, 3: 15}
# if keys are duplicate then the values will override and latest key-value will be treated as the element to retrive
print(sample_dict[3])

sample_dict = {(1, 2, 3, 4): 1, 2: 4, 3: 9}
print(sample_dict[(1, 2, 3, 4)])

sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict["1"])

# sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
# print(sample_dict[[1, 2, 3, 4]])

"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/05_dict.py", line 11, in <module>
    sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
TypeError: unhashable type: 'list'
"""
dict_keys = sample_dict.keys()
print("Dict keys:",dict_keys)
dict_values = sample_dict.values()
print("Dict values:",dict_values)
dict_items = sample_dict.items()
print("Dict items:", dict_items)

# What happens if you access a key that is not present inside a dict
sample_dict = {"1": 1, 2: 4, 3: 9}
print("Using get():",sample_dict.get(1)) # None
# get method will return None if the element is not present in the dict.

# print(sample_dict[1]) # throws an Error
""" 
Traceback (most recent call last):
  File "D:\Personal\DevOps\JoinDevOps-SivaKumarReddy\shell-script-repo\python-repo\05_dict.py", line 36, in <module>
    print(sample_dict[1]) # throws an Error
          ~~~~~~~~~~~^^^
KeyError: 1 
"""


sample_dict = {1: 1, 2: 4, 3: 9}
sample_dict[4] = 16     ## adding an element to the dict
print(sample_dict)
