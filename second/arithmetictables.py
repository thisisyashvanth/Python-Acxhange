class Recursion:

    def multiplication(self, num, i=1):
        if i > 10:
            return
        print(f"{num} * {i} = {num * i}")
        self.multiplication(num, i + 1)

    def division(self, num, i=1):
        if i > 10:
            return
        print(f"{num} / {i} = {num / i:.2f}")
        self.division(num, i + 1)

    def addition(self, num, i=1):
        if i > 10:
            return
        print(f"{num} + {i} = {num + i}")
        self.addition(num, i + 1)

    def subtraction(self, num, i=1):
        if i > 10:
            return
        print(f"{num} - {i} = {num - i}")
        self.subtraction(num, i + 1)


class Loop:

    def multiplication(self, num):
        for i in range(1, 11):
            print(f"{num} * {i} = {num * i}")

    def division(self, num):
        for i in range(1, 11):
            print(f"{num} / {i} = {num / i:.2f}")

    def addition(self, num):
        for i in range(1, 11):
            print(f"{num} + {i} = {num + i}")

    def subtraction(self, num):
        for i in range(1, 11):
            print(f"{num} - {i} = {num - i}")


num = int(input("Enter a number: "))

recursion = Recursion()
loop = Loop()


print("\nUsing Recursion")

print("\nMultiplication Table")
recursion.multiplication(num)

print("\nDivision Table")
recursion.division(num)

print("\nAddition Table")
recursion.addition(num)

print("\nSubtraction Table")
recursion.subtraction(num)


print("\nUsing Loops")

print("\nMultiplication Table")
loop.multiplication(num)

print("\nDivision Table")
loop.division(num)

print("\nAddition Table")
loop.addition(num)

print("\nSubtraction Table")
loop.subtraction(num)