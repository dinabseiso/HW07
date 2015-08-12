#!/usr/bin/env python
# HW07_ex10_06.py

# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()



### Imports go here. 

### Body goes here. 

def is_sorted(variousLists):
	if variousLists == sorted(variousLists):	# A rather simple, but powerful way to check whether a list is sorted...
		return True
	else : 
		return False 

### Call your functions through main()

def main():
	pass


### Bootstrap goes here

if __name__ == "__main__" : 
	main()