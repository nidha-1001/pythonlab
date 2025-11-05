def add(*n):
    """Adds all given numbers."""
    return sum(n)

nums = input("Enter numbers separated by space: ").split()
nums = [int(x) for x in nums]

print("Sum =", add(*nums))
