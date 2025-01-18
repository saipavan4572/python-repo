# Create a list
# List is a mutable datatype
sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"] # list()
print(sample_list)

# Indexing, slicing
sample_ele = sample_list[1]
print(sample_ele)

# sample_ele = sample_list[5]   # here the index should be length-1 => 4
# print(sample_ele)

"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/04_list.py", line 9, in <module>
    sample_ele = sample_list[5]
IndexError: list index out of range
"""

sample_ele = sample_list[len(sample_list) - 1] # sample_list[-1]
print("last element is:",sample_ele)

# Slicing
sliced_list = sample_list[1:3] # ("Terraform", "Jenkins")
print("sliced list:",sliced_list)

sliced_list_len = len(sliced_list)
print("length of sliced list:",sliced_list_len)

# List is a mutable data type
# Once defined, it can be altered
sample_list[1] = "Shell"
print(sample_list)

# Append element to the list
sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]
print("List elements:",sample_list)
sample_list.append("Shell") # inplace operation
print("List elements after appending new element:\n",sample_list)

# Append list to list
# If a list is appended to an existing list using append method then new list will contains with existing list elements + new list as single element to the existing list.
# l1=[1,2,3] l2=[3,4,5]
# l1.append(l2) ===>    newlist =[1,2,3,[3,4,5]]
sample_list.append(sample_list)
print(sample_list)
print(len(sample_list))

last_element = sample_list[len(sample_list) - 1]
print(last_element)

# extend
sample_list = [1, 2, 'sample', True]
sample_list.extend(sample_list)
print(len(sample_list), sample_list)
# If a list is added to an existing list using extend method then new list will contains with existing list elements + new list elements will added as list as separate elements to the existing list.
# l1=[1,2,3] l2=[3,4,5]
# l1.extend(l2) ===>    newlist =[1,2,3,3,4,5]


# membership operator: in, not in
is_elem = 2 in sample_list
print("Is elements 2 exist the list: ",is_elem)

is_elem = False in sample_list
print("Is elements False exist the list: ",is_elem)