nums = list(map(int, input("Enter numbers: ").split()))
pos = [x for x in nums if x > 0]
print(pos)

n = int(input("Enter N: "))
squares = [x**2 for x in range(1, n+1)]
print(squares)

word = input("Enter a word: ")
vowels = [x for x in word if x in 'aeiouAEIOU']
print(vowels)

word = input("Enter a word: ")
ordinals = [ord(x) for x in word]
print(ordinals)
