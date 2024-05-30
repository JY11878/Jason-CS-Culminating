# Bubble Sort
nums = [6, 3, 2, 1, 9, 11, 20]

try:
    # Check if input is a list
    if type(nums) != list:
        print(TypeError("Input is not a list"))

    # Get the length of the list
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if nums[j] > nums[j + 1]:
                # Swap if elements are in wrong order
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print("Sorted list", nums)

except TypeError as err:
    # Handle TypeError
    print("Error:", err)
except ValueError as err:
    # Handle ValueError
    print("Error:", err)


