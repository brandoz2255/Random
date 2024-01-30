
# Brandon Sanchez 
# 55
# 11/1/2023
# Lab 10

# Remark: This program allows the user to input fruit names and their corresponding weights, and then displays the list of fruits and their weights.

# Remark: Create the user greeting.
print("Welcome to the Fruit Weight Tracker!")

# Remark: Initialize/create two empty lists.
fruit_types = []
fruit_weights = []

# Remark: Initialize/create a variable to control the user input loop.
continue_input = True

# Remark: Create the user input loop.
while continue_input:
    # Remark: Get the input for fruit type.
    fruit_name = input("Enter a fruit name (or press Enter to exit): ")

    if fruit_name == "":
        continue_input = False
    else:
        # Remark: Get the input for weight.
        fruit_weight = float(input(f"Enter the weight of {fruit_name} in pounds: "))
        fruit_types.append(fruit_name)
        fruit_weights.append(fruit_weight)

# Remark: Initialize/create a variable for the index value to control the print loop.
index = 0

# Remark: Create the loop that will iterate through and display each list item from each list.
print("\nFruit Weight List:")
print("----------------------------")
for index in range(len(fruit_types)):
    print("{:<20} {:>10} lbs.".format(fruit_types[index], fruit_weights[index]))

# Remark: Display the closing message.
print("\nThank you for using the Fruit Weight Tracker!")

