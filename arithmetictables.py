# num = int(input("Enter a number: "))

# print("\nAddition Table")
# for i in range(1, 11):
#     print(f"{num} + {i} = {num + i}")

# print("\nMultiplication Table")
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

# print("\nSubtraction Table")
# for i in range(1, 11):
#     print(f"{num} - {i} = {num - i}")

# print("\nDivision Table")
# for i in range(1, 11):
#     print(f"{num} / {i} = {num / i:.2f}")

def multiplication(num, i=1):
    if i > 10:
        return
    print(f"{num}*{i} = {num * i}")
    multiplication(num, i+1)

def division(num, i=1):
    if i > 10:
        return
    print(f"{num}/{i} = {num / i:.2f}")
    division(num, i+1)

def addition(num, i=1):
    if i > 10:
        return
    print(f"{num}+{i} = {num + i}")
    addition(num, i+1)

def subtraction(num, i=1):
    if i > 10:
        return
    print(f"{num}-{i} = {num - i}")
    subtraction(num, i+1)

num = int(input("Enter a number: "))
print("Multiplication Table")
multiply = multiplication(num)
print()

print("Division Table")
divide = division(num)
print()

print("Addition Table")
add = addition(num)
print()

print("Subtraction Table")
subtract = subtraction(num)
print()