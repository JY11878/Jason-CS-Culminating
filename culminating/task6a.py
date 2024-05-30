# error handling example
try:
    file = open("file000", "r")
except FileNotFoundError:
    print("The file is not exist.")
