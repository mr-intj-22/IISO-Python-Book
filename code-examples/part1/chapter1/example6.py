'''
Exercise 6: Logical Error Identification
Objective: Identify and fix logical errors in code.
'''


# Intentional Logical Error
def calculate_average(a, b, c):
    return (a + b + c) / 2  # Incorrect formula for average


average = calculate_average(10, 20, 30)
print("The average is:", average)
