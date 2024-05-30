# factorial calculator
def factorial(num):
    # Base case
    if num == 0:
        return 1
    else:
        # Recursive case
        return num * factorial(num - 1)

# Example
inputNumber = 5
print("Factorial of", inputNumber, "is", factorial(inputNumber))
# user input
inputNumber = int(input("Enter a number: "))
print("Factorial of", inputNumber, "is", factorial(inputNumber))

