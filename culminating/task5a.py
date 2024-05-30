# read data from a file and write the data to another file
# Open the input file for reading
with open("input.txt", "r") as inputFile:
    # Read the data from the input file
    data = inputFile.read()

# Print the data
print(data)

# Open the output file for writing
with open(
        "output.txt", "w") as outputFile:
    # Write the processed data to the output file
    outputFile.writelines(data)

# Print confirmation message
print("above data has been written to output.txt!")

