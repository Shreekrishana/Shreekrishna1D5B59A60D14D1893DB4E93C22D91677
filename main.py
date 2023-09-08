#Implement a recursive function to calculate a factorial of a given number in python program

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
  