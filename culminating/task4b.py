# Fibonacci Calculator
def fibonacci(pos):
    # Base case
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# example
inputPos = 6
print("Fibonacci number at", inputPos, "is", fibonacci(inputPos))
# user input
inputPos = int(input("Enter a position: "))
print("Fibonacci number at", inputPos, "is", fibonacci(inputPos))

