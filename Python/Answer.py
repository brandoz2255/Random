def sum_even_numbers(numbers):
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
    return even_sum

numbers = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(numbers)
print(f"The sum of even numbers is: {result}")
