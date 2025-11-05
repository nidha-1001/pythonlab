def interest(p, t, senior):
    rate = 12 if senior else 10
    return (p * rate * t) / 100

p = float(input("Enter principal amount: "))
t = float(input("Enter time (in years): "))
senior = input("Senior citizen (yes/no): ").lower() == "yes"

si = interest(p, t, senior)
print("Simple Interest =", si)
