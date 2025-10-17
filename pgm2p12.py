numbers = input("Enter integers separated by commas: ").split(',')
numbers = [int(num.strip()) for num in numbers]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("list after removing even numbers:",odd_numbers)
