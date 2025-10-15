
list1 = list(map(int, input("Enter first list (space-separated): ").split()))
list2 = list(map(int, input("Enter second list (space-separated): ").split()))


if len(list1) == len(list2):
    print("Same length")
else:
    print("Different length")


if sum(list1) == sum(list2):
    print("Sums are equal")
else:
    print("Sums differ")


common = set(list1) & set(list2)
if common:
    print("Common values:", common)
else:
    print("No common values")


