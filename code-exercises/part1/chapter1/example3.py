'''
Exercise 3: Handling Logical Errors
Objective: Identify and fix logical errors in Python code.
'''


# Example Solution:
def calculate_area(length, width):
    return length * width  # Correct formula for area


# Intentional Logical Error (Uncomment to see the error)
# def calculate_area(length, width):
#     return length + width  # Incorrect formula
area = calculate_area(5, 10)
print("The area of the rectangle is:", area)
