'''
Exercise 8: Logical Error with Division by Zero
Objective: Identify and fix a logical error involving division by zero.
'''


# Intentional Logical Error (Division by Zero)
def divide(a, b):
    return a / b


result = divide(10, 0)
print(result)
