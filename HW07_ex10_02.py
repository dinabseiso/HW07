#!/usr/bin/env python
# HW07_ex10_02.py

# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


### Imports go here. 

### Body goes here. 

def capitalize_nested(words):
	capitalized = words
	i = 0
	for improper in words: 
		beginning = improper[0]							# I do not know how to isolate the first character in capitalization, otherwise.
		end = improper[1:]
		if isinstance(improper, list):
			capitalize_nested(improper)					# Nothing needs to be returned, as nothing is being compounded. See below.
			i += 1
		else: 
			beginning = beginning.upper()				
			proper = beginning + end
			words[i] = proper							# The capitalization is immediately being dealt with here, as opposed to storing for later use.
			i += 1
	return words
				


### Call your functions in main()

def main(): 
	pass

	
## Bootstrap

if __name__ == '__main__':
    main()