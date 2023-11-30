Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ################################################################################
... Day 8: How many cans of paint do we need to paint the entire wall in question - problem
... 
... # Step 1 - Import the module for rounding numbers to the next integer number
... import math
... 
... # Step 2 - Define the function and its parameters
... def paint_calc(height, width, cover): # Formula calculation
...   num_cans = (height * width) / cover 
...   round_up_cans = math.ceil(num_cans) # rounding step
...   print(f"You'll need {round_up_cans} cans of paint.") # Print the result statement
... 
... # Step 3 - Define the parameter input
... test_h = int(input()) # Height of wall (m) # test height
... test_w = int(input()) # Width of wall (m) # test weight
... coverage = 5 # coverage of paint per unit of wall
