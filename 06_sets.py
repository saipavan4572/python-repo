sample_set = {1, 2, 5, 2, 4, 3, 4, 2} # set()
print(sample_set)

# A Set returns unique elements that is stored inside that variable
# Sets don't consider the order of insertion
# Sets don't support indexing

# Add elements to a set
sample_set = {1, 2, 5, 2, 4, 3}
print(sample_set)
sample_set.add(6)
print("after adding new element to the set:\n",sample_set)

#print(sample_set[2])   #Error ==> we can't get specific element from set.
""" 
Traceback (most recent call last):
  File "D:\Personal\DevOps\JoinDevOps-SivaKumarReddy\shell-script-repo\python-repo\06_sets.py", line 13, in <module>
    print(sample_set[2])
          ~~~~~~~~~~^^^
TypeError: 'set' object is not subscriptable
 """