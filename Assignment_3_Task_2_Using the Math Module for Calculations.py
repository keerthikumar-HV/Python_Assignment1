import math

# Ask user for input
number = float(input("Enter a number: "))

# Calculations using math module
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Display results
print(f"Square root of {number} is {square_root}")
print(f"Natural logarithm of {number} is {natural_log}")
print(f"Sine of {number} (in radians) is {sine_value}")
