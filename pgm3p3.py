numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
total = 0
for i in numbers:
    total += i
print("Sum of all items:", total)

