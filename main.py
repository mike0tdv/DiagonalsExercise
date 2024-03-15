import random

# Declaring the 2D - list
arr = []

# Declaring the variables
d1_sum = 0
d2_sum = 0
used_values = set()  # Set to store used values

# The user is giving the dimensions
row = int(input("Enter the rows of the list: "))
cols = int(input("Enter the columns of the list: "))

# Filling the list with random values
for row in range(row):
    arr1 = []
    for col in range(cols):
        while True:
            new_value = random.randint(1, 999)
            if new_value not in used_values:
                used_values.add(new_value)
                arr1.append(new_value)
                break
    arr.append(arr1)

# Getting the sum of the two diagonals
for i in range(len(arr)):
    d1_sum += arr[i][i]
    d2_sum += arr[i][len(arr) - 1 - i]

# Printing the values of the list and the sums
separator = ' ' * 5
for row in arr:
    print(separator.join(map(str, row)))
print()
print(f"The sum of the numbers in the first diagonal is: {d1_sum}")
print(f"The sum of the numbers in the second diagonal is: {d2_sum}")