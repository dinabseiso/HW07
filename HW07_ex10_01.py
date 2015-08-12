#!/usr/bin/env python
# HW07_ex10_01.py

# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

### Imports go here. 

### Body goes here. 


def nested_sum(variousLists):
	nestedSum = 0
	for index in variousLists : 
		if isinstance(index, list): 		# isinstance is used to verify whether the passed in object is of the type specified.
			nestedSum += nested_sum(index)	# If the index is indeed a list, recursion occurs and returns the summated value.
		else:
			nestedSum += index				
	return nested_sum						# Summation returned for manipulation outside of the function.  




### Call your functions in main()

def main(): 
	pass
	
## Bootstrap

if __name__ == '__main__':
    main()