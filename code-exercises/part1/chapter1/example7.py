'''
Exercise 7: Debugging Syntax Errors with Tracebacks
Objective: Use tracebacks to identify and fix syntax errors.
'''


# Intentional Syntax Error
def print_message(message):
    print("Message: " message)  # Missing + operator


print_message("Hello, world!")
