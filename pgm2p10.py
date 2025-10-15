color_list1 = input("Enter colors for list 1 (separated by space): ").split()
color_list2 = input("Enter colors for list 2 (separated by space): ").split()

result = [color for color in color_list1 if color not in color_list2]

print("Colors in list1 not in list2:", result)
