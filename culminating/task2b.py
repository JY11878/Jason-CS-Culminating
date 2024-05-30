# Selection Sort
nums = [6, 3, 2, 1, 9, 11, 20]

try:
    # Check if input is a list
    if type(nums) != list:
        print(TypeError("Input must be a list"))

    # Get the length of the list
    n = len(nums)
    for i in range(n):
        # Assume the minimum is the first element
        minIdx = i
        for j in range(i+1, n):
            # Find the actual minimum element
            if nums[j] < nums[minIdx]:
                minIdx = j
        # Swap the found minimum element with the first element
        nums[i], nums[minIdx] = nums[minIdx], nums[i]
    print("Sorted list:", nums)

except TypeError as err:
    # Handle TypeError
    print("Error:", err)
except ValueError as err:
    # Handle ValueError
    print("Error:", err)

