# Write a python function to remove duplicates from a dictionary

#   data = [
# {"id": 1, "name": "Alice"}, 
#   {"id": 2, "name": "Bob"},
#  {"id": 1, "name": "Charlie"}, 
#  {"id": 3, "name": "Alice"}
#  ]

# Write a Python code to print the factorial 
# Formula : n! = n*(n-1)*....*1(base : 0! = 1)

# Take the input from the user as n , 

# Example : 
# Input : 5
# Output : 120

def factorial(n):
    if n ==0  or n == 1:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter a number to find its factorial: "))
print(factorial(n))