
# Brandon Sanchez
#55
# 9/27/2023
#Lab 4


# Remark: This program converts degrees Celsius to degrees Fahrenheit.

# User greeting
print("\nThis program will convert degrees Celsius to degrees Fahrenheit.")

# Get user input and assign to a variable (float data type)
celsius = float(input("\nPlease enter the temperature in degrees Celsius; you may use decimals: "))

# Perform the temperature conversion and assign the result to a variable
fahrenheit = (celsius * 9/5) + 32

# Display the results with one decimal point
print("\n {:.1f} degrees Celsius is equal to {:.1f} degrees Fahrenheit.".format(celsius, fahrenheit))

# Exit message
print("\nHave a great day!\n")
