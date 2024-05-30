# find target element in a sorted list
# example list
sortedList = [1,2,3,4,5,6,7,8,9]
target = 6

try:
    # Check if the list is sorted
    for i in range(len(sortedList) - 1):
        if sortedList[i] > sortedList[i + 1]:
            print(ValueError("The list is not sorted"))
    ls = 0
    rs = len(sortedList) - 1
    target_element_exists = False

    while ls <= rs:
        mid = (ls + rs) // 2
        middleValue = sortedList[mid]

        if middleValue == target:
            print(f"Target at index {mid}")
            targetExist = True
            break
        elif middleValue < target:
            # Search in the right half
            ls = mid + 1
        else:
            # Search in the left half
            rs = mid - 1

    if not targetExist:
        print("Target element is not exist")

except ValueError as err:
    print(f"Error: {err}")
