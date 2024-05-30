# Define Students class
class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create a list
studentList = [Students("Jason", 19), Students("Will", 15), Students("Alex", 18)]

try:
    # Check if input is a list
    if type(studentList) != list:
        print(TypeError("Input is not a list"))

    # Get the length of the list
    n = len(studentList)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare ages of adjacent students
            if studentList[j].age > studentList[j + 1].age:
                # Swap if ages are in the wrong order
                studentList[j], studentList[j + 1] = studentList[j + 1], studentList[j]

    # Print sorted student list
    for student in studentList:
        print(student.name, student.age)

except TypeError as err:
    # Handle TypeError
    print("Error:", err)
except ValueError as err:
    # Handle ValueError
    print("Error:", err)
