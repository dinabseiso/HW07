#!/usr/bin/env python
# HW07_ex10_03.py

# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()



### Imports go here. 
import copy as copy

### Body goes here. 

def cumulative_sum(variousLists):
	sumList = []
#	sumList = variousLists[:]					# Because lists are not immutable, I copied the original list into a new one.
	sumList = copy.copy(variousLists)			# This is an alternative way to copy one list as another.
	for i in range(len(variousLists)-1) : 
		combined = sumList[i] + sumList[i+1]	# From the copied and continuously updated list, consecutively add.
		sumList[i+1] = combined					# Replace the appropriate index with the updated sum.
	return sumList								# For future printing by Daniel.



### Call your functions in main()

def main(): 
	pass

## Bootstrap

if __name__ == '__main__':
    main()