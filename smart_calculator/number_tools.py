# NUMBER ANALYSIS MODULE
# Checks number properties

def check_number(n):
    # checks if number is positive, negative or zero
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"

def check_even_odd(n):
    # checks parity of number
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
