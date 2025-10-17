words = input("Enter words separated by spaces: ").split()
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
print("print the length of the longest word is:",max_length)
