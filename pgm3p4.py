import math


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("4-digit perfect squares with all even digits:")

found = False  # To check if we found any valid number


for num in range(start, end + 1):
    # Check if number is a perfect square
    if math.isqrt(num) ** 2 == num:
        # Check if all digits are even
        if all(int(digit) % 2 == 0 for digit in str(num)):
            print(num)
            found = True
if not found:
    print("No perfect squares with all even digits found in this range.")

