def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from the user
number = int(input("Enter a number: "))

# Calculate factorial
output = factorial(number)

# Print result
print(f"Factorial of {number} is {output}")
