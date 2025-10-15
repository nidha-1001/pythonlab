num = input("enter integerss separated by spaces:").split()
result= [ int(n) if int(n)<= 100 else 'over' for n in num ]
print(result)

