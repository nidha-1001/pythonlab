names_input = input("Enter first names: ")
first_names = names_input.split()
count_a = sum(name.lower().count('a') for name in first_names)
print("Total occurrences of 'a':", count_a)
