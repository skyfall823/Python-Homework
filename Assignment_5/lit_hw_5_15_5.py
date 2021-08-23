"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 10 August 2021
Homework Problem # 5
Description of Problem : Prompt the user to enter a factorial starting\
integer. Calculate the result with and without recursion.
"""
# Recursive factorial function
def factorial(n):
   if n == 1:               
       return n
   else:
       return n * factorial(n - 1)      
       
# Non-recursive factorial function       
def factorial2(n):
    value = 1;                  
    for i in range(1, n + 1):      
        value = value * i;
    return value;

# Validate data entry
while True:
    #ask the user to input the number
    number = int(input("Please Input A Positive Integer Number : "));
    if number < 0:              
        print("Factorial does not work with negative numbers. Please Enter A Positive Number!");
        continue
    elif number == 0:
        print("The factorial of 0 is 1. Please Enter A Positive Number!");
        continue
    else:
        break     

# Calling recursive function and print the result
result = factorial(number);
print("The factorial of", number, "using Recursive function is :", f"{result:,}")

# Calling non-recursive function and print the result
result = factorial2(number);
print("The factorial of", number, "using Non-Recursive function is :", f"{result:,}")