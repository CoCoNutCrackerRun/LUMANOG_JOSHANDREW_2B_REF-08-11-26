class Comparator:
    def compare(self):
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))

        if num1 > num2:
            print(f"The bigger number is: {num1}")
        elif num2 > num1:
            print(f"The bigger number is: {num2}")
        else:
            print("Both numbers are equal.")

com = Comparator()
com.compare()