total = 0
inputs = []

while True:
    user_input = input("Enter a number (or type 'stop' to end): ")
    if user_input.lower() == "stop":
        print("I will see you again... but not yet... not yet.")
        break

    try:
        number = int(user_input)
        inputs.append(number)
        if number == 0:
            total = 0
            print("The total has been reset to 0")
        elif number % 2 == 0:
            total += number
            print(f"{number} is even. Total: {total}")
        else:
            total -= number
            print(f"{number} is odd. Total: {total}")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
print("All inputs: ")
if inputs:
    for i in inputs:
        print(i)
else:
    print("No valid numbers were entered.")

# Can also be (This is shorter):
# print("All inputs: ")
# for i in inputs:
#     print(i)
#
# or can also be (This will be messy to look at and read | Will still run, but will show "All inputs: [number in list]" for all numbers that are in the list):
# for i in inputs:
#     print(f"All inputs: {i}")