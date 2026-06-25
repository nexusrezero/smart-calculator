# CALCULATOR MODULE
# Handles all math operations

def add(a, b):  
    return a + b # returns sum

def subtract(a, b):
    return a - b # returns difference

def multiply(a, b):
    return a * b  # returns sum

def divide(a, b):
 # prevents division by zero error
    if b == 0:
        return "Cannot divide by zero"
    return a / b
