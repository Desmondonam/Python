weight = int(input("Enter your wight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight = weight / 0.45
    print(f"You are {converted} pounds")