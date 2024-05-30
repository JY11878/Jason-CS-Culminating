# file error handling
try:
    file = open("file123","r")
    data = file.read()
except FileNotFoundError:
    print("The file was not found.")
except IOError:
    print("An I/O error occurred.")
finally:
    file.close()
