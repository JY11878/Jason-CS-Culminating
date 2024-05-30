# FileNotFoundError
try:
    file = open("ghostFile", "r")
except FileNotFoundError:
    print("File is not exist.")

# IOError
try:
    file = open("errorFile.txt", "r")
    data = file.read()
except IOError:
    print("An I/O error occurred.")

# ValueError
try:
    number = int("I am a string")
except ValueError:
    print("invalid data type")

# TypeError
try:
    result = "string" + 1
except TypeError:
    print("cannot add a string to an integer")






