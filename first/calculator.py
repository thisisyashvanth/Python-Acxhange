class Operations:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        try:
            return self.num1 / self.num2
        except Exception as e:
            return e
        
    def exponent(self):
        return pow(self.num1, self.num2)
    
    def modulus(self):
        return self.num1 % self.num2

print("\nCalculator")
print("-----------------------------")

while True:
    print("What do you want to perform ? ")
    choice = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponent\n6. Modulus\n7. Exit\n\n"))
    
    if choice == 7:
        print("GudBye")
        break

    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    operations = Operations(num1, num2)

    match choice:
        case 1:
            print(f"{operations.add()}\n")
        case 2:
            print(f"{operations.subtract()}\n")
        case 3:
            print(f"{operations.multiply()}\n")
        case 4:
            print(f"{operations.divide()}\n")
        case 5:
            print(f"{operations.exponent()}\n")
        case 6:
            print(f"{operations.modulus()}\n")
        case _:
            print("Enter a valid choice")