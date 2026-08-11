total = 0
inputs = []

while True:
    user_input = input("Enter a number (or type 'stop' to end): ")
    if user_input.lower() == "stop":
        print("You typed 'stop'. The program is ending!")
        break

    try:
        number = int(user_input)
        inputs.append(number)
        if number == 0:
            total = 0
            print("The total has been reset to 0")
        elif number % 2 == 0:
            total += number
            print(f"{number} is EVEN → Added. Running total: {total}")
        else:
            total -= number
            print(f"{number} is ODD → Subtracted. Running total: {total}")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
print("--- Summary of all numbers you entered ---")
if inputs:
    for i in inputs:
        if i == 0:
            print(f"{i} → Reset")
        elif i % 2 == 0:
            print(f"{i} → Even (was added)")
        else:
            print(f"{i} → Odd (was subtracted)")
else:
    print("No valid numbers were entered.")

print(f"Final Total: {total}")