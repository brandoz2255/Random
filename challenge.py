

print("Hello! This program will take a list of numbers and then calculate the sum of all the numbers in the list, as well as the sum of even numbers.")

list = []
list_2 = []

run_input = True

while run_input:
    number_input = input("\nEnter a number to add (press enter to quit): ")
    
    if number_input == "":
        run_input = False
    else:
        user_input = float(number_input)
        
        if user_input % 2 == 0:
            print(f"\nThis number is even: {user_input}")
            list_2.append(user_input)
        else:
            print(f"\nYou've added {user_input}.")
            list.append(user_input)

total = sum(list)
total_2 = sum(list_2)

print(f"\nThe total of your list is: {total}")
print(f"\nThe even total is: {total_2}")

