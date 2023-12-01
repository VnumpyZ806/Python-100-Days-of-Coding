# Python-100-Days-of-Coding
Simple projects completed through Udemy course '100 days of Code: The complete Python Pro Bootcamp'


Examples:

___
Day 8: How many cans of paint do we need to paint the entire wall in question - problem

# Step 1 - Import the module for rounding numbers to the next integer number
`import math`

# Step 2 - Define the function and its parameters
`def paint_calc(height, width, cover): # Formula calculation`  
`  num_cans = (height * width) / cover`  
`  round_up_cans = math.ceil(num_cans) # rounding step`  
`  print(f"You'll need {round_up_cans} cans of paint.") # Print the result statement`  

# Step 3 - Define the parameter input
`test_h = int(input()) # Height of wall (m) # test height`  
`test_w = int(input()) # Width of wall (m) # test weight`  
`coverage = 5 # coverage of paint per unit of wall`  
`paint_calc(height=test_h, width=test_w, cover=coverage) # formula input to test the expected output`  

___


Day 8.2: Check if your number is a prime number or not

`def prime_checker(number):`  
`  is_prime = True`  
`  for i in range(2, number):`  
`    if number % i == 0:`  
`      is_prime = False`  
`  if is_prime:`  
`    print("It's a prime number.")`  
`  else:`  
`    print("It's not a prime number.")`  


`n = int(input()) # Check this number` 
`prime_checker(number=n)`

___











