num = int(input("enter a number:"))
i = 1
print("factors of", num, "are:")
while i <= num:
     if num % i == 0:
          print(i)
          i = i + 1
