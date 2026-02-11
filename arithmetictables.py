num = int(input("Enter a number: "))

print("\nAddition Table")
for i in range(1, 11):
    print(f"{num} + {i} = {num + i}")

print("\nMultiplication Table")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

print("\nSubtraction Table")
for i in range(1, 11):
    print(f"{num} - {i} = {num - i}")

print("\nDivision Table")
for i in range(1, 11):
    print(f"{num} / {i} = {num / i:.2f}")