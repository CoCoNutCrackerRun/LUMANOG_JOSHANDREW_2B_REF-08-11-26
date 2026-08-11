total = 0
inputs = []

while True:
    user_input = input("Please enter a number (or 'stop' to quit): ")
    if user_input.lower() == "stop":
        print("You typed stop. Program ending.")
        break

    try:
        number = int(user_input)
        inputs.append(number)

        if number == 0:
            total = 0
            print("You entered 0. Total has been reset to 0.")
        elif number % 2 == 0:
            total += number
            print(f"{number} is EVEN. Added. Running total: {total}")
        else:
            total -= number
            print(f"{number} is ODD. Subracted. Running total: {total}")
    except ValueError:
        print("Invalid. Please enter a number.")

print("---SUMMARY---")
if len(inputs) == 0:
    print("You did not enter any number.")
else:
    for num in inputs:
        if num == 0:
            print(f"{num} Reset the total")
        elif num % 2 == 0:
            print(f"{num} Even (Added)")
        else:
            print(f"{num} Odd (Subracted)")

print(f"Final Total: {total}")
print("Thanks for using the program")