import sys
import math
import random
import functools

print = functools.partial(print, flush=True)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt + " "))
        except ValueError:
            print("Invalid input. Please enter a number (e.g.: 3, 5)")
        except EOFError:
            print("\nNo input received. Exiting program.")
            raise SystemExit


def get_int(prompt):
    while True:
        try:
            return int(input(prompt + " "))
        except ValueError:
            print("Invalid input. Please enter a number (e.g.: 3, 5)")
        except EOFError:
            print("\nNo input received. Exiting program.")
            raise SystemExit


def safe_input(prompt):
    try:
        return input(prompt + " ")
    except EOFError:
        print("\nNo input received. Exiting program.")
        raise SystemExit


def pause():
    safe_input("\nPress ENTER to return to the menu...")


def print_header(title):
    print("\n" + "=" * 70)
    print(f"{title}")
    print("=" * 70)


def demo_constants():
    # PI MEASUREMENT
    print("math.pi ->", math.pi)

    # RADIANS AND DEGREE MEASUREMENT
    angle_in_radians = math.radians(45)
    print(f"math.radians(45) -> {angle_in_radians}")
    print(f"math.degrees({angle_in_radians:.4f}) -> {math.degrees(angle_in_radians)}")

    # TRIGONOMETRY (SIN, COS, TAN)
    print(f"math.sin(45°) -> {math.sin(angle_in_radians)}")
    print(f"math.cos(45°) -> {math.cos(angle_in_radians)}")
    print(f"math.tan(45°) -> {math.tan(angle_in_radians)}")

    # INVERSE VERSIONS (SIN, COS, TAN)
    print(f"math.asin(0.5) -> {math.asin(0.5)} radians")
    print(f"math.acos(0.5) -> {math.acos(0.5)} radians")
    print(f"math.atan(0.5) -> {math.atan(0.5)} radians")

    # HYPERBOLIC FUNCTIONS
    print(f"math.sinh(1.0) -> {math.sinh(1.0)}")
    print(f"math.cosh(1.0) -> {math.cosh(1.0)}")
    print(f"math.tanh(1.0) -> {math.tanh(1.0)}")

    # INVERSE HYPERBOLIC FUNCTIONS
    print(f"math.asinh(1.0) -> {math.asinh(1.0)}")
    print(f"math.acosh(1.5) -> {math.acosh(1.5)}")
    print(f"math.atanh(0.5) -> {math.atanh(0.5)}")

    # EXPONENTIAL AND LOGARITHMIC FUNCTIONS
    print("math.e ->", math.e)
    print(f"math.exp(1) -> {math.exp(1)}")
    print(f"math.exp(2) -> {math.exp(2)}")
    print(f"math.log(math.e) -> {math.log(math.e)}")
    print(f"math.log(8, 2) -> {math.log(8, 2)}")
    print(f"math.log10(1000) -> {math.log10(1000)}")
    print(f"math.log2(8) -> {math.log2(8)}")

#SECTION1
def trig_menu():
    print_header("TRIGONOMETRIC (CIRCULAR) FUNCTIONS")
    print("""1. Show the value of pi
2. Convert degrees -> radians
3. Convert radians -> degrees
4. Compute sin, cos, tan of an angle (The user must enter a number in degrees)
5. Compute asin, acos, atan of a value (-1 to 1 for asin/acos)
0. Back to main menu
""")

    choice = safe_input("Enter your choice:").strip()

    if choice == "1":
        print(f"\nmath.pi = {math.pi}")

    elif choice == "2":
        deg = get_float("Enter an angle in degrees:")
        rad = math.radians(deg)
        print(f"\n{deg} degrees = {rad} radians")

    elif choice == "3":
        rad = get_float("Enter an angle in radians:")
        deg = math.degrees(rad)
        print(f"\n{rad} radians = {deg} degrees")

    elif choice == "4":
        deg = get_float("Enter an angle in degrees:")
        rad = math.radians(deg)
        print(f"\nAngle = {deg} degrees ({rad} radians)")
        print(f"sin({deg}) = {math.sin(rad)}")
        print(f"cos({deg}) = {math.cos(rad)}")
        print(f"tan({deg}) = {math.tan(rad)}")

    elif choice == "5":
        val = get_float("Enter a value:")
        print()
        try:
            result = math.asin(val)
            print(f"asin({val}) = {result} radians, {math.degrees(result)} degrees")
        except ValueError:
            print("asin(x) needs -1 <= x <= 1. Skipped.")

        try:
            result = math.acos(val)
            print(f"acos({val}) = {result} radians, {math.degrees(result)} degrees")
        except ValueError:
            print("acos(x) needs -1 <= x <= 1. Skipped.")

        result = math.atan(val)
        print(f"atan({val}) = {result} radians, {math.degrees(result)} degrees")

    elif choice == "0":
        return

    else:
        print("\nInvalid Choice.")

    pause()

#SECTION2
def hyperbolic_menu():
    print_header ("HYPERBOLIC FUNCTIONS")
    print ("""1. Show the value of e
2. Compute sinh, cosh, tanh of a value
3. Compute asinh, acosh, atanh of a value (acosh needs x >= 1, atanh needs -1 < x < 1)
0. Back to main menu
""")

    choice = safe_input("Enter your choice:").strip()
    if choice == "1":
        print (f"\nmath.e = {math.e}")

    elif choice == "2":
        val = get_float("Enter a value: ")
        print (f"\nValue = {val}")
        print (f"sinh({val}) = {math.sinh(val)}")
        print (f"cosh({val}) = {math.cosh(val)}")
        print (f"tanh({val}) = {math.tanh(val)}")

    elif choice == "3":
        val = get_float("Enter a value")
        print()
        print (f"asinh({val}) = {math.asinh(val)}")
        try:
            print (f"acosh({val}) = {math.acosh(val)}")
        except ValueError:
            print ("acosh(x) needs x >= 1. Skipped.")
        try:
            print (f"atanh({val}) = {math.atanh(val)}")
        except ValueError:
            print ("atanh(x) needs -1 < x < 1. Skipped.")

    elif choice == "0":
        return

    else:
        print ("\nInvalid Choice.")

    pause()

#SECTION3
def exponent_menu():
    print_header ("EXPONETIAtION AND LOGARITHMS FUNCTIONS")
    print ("""1. Show the value of e
    2. Compute exp (x)
    3. Compute the natural log, log10, log2 of a value
    4. Compute log(x, base) with a custom base
    5. Compute pow(x, y) - built-in vs math.pow
    0. Back to main menu
    """)

    choice = safe_input ("Enter your choice: ").strip()

    if choice == "1":
        print (f"\nmath.e = {math.e}")

    elif choice == "2":
        x = get_float("Enter x: ")
        print (f"nexp ({x}) = e^{x} = {math.exp(x)}")

    elif choice == "3":
        x = get_float("Enter a positive numver x: ")
        try:
            print (f"\nlog({x}) = {math.log(x)}")
            print (f"log10({x}) = {math.log10(x)}")
            print (f"log2({x}) = {math.log2(x)}")
        except ValueError:
            print ("Logarithms require x > 0. Please try again.")

    elif choice == "4":
        x = get_float("Enter x (must be > 0): ")
        b = get_float("Enter the base b (must be > 0 and != 1): ")
        try:
            print (f"\nlog({x}), base = {b} = {math.log(x, b)}")
        except (ValueError, ZeroDivisionError):
            print ("Invalid input for for a logarithm with that base.")

    elif choice == "5":
        x = get_float("Enter the base x: ")
        y = get_float("Enter the exponet y: ")
        print (f"Built-in pow({x}, {y}) = {pow(x, y)}")
        print (f"math.pow({x}, {y}) = {math.pow(x, y)}")
        print ("(Note: pow( can return an int for integer inputs); "
               "math.pow() always returns a float.)")

    elif choice == "0":
        return

    else:
        print ("\nInvalid Choice")

    pause()

#SECTION4
def general_menu():
    print_header("GENERAL-PURPOSE MATH FUNCTIONS")
    print("""1. Compute ceil, floor, and trunc of a value
2. Compute a factorial
3. Compute the hypotenuse of a right triangle
0. Back to Main Menu
""")

    choice = safe_input("Enter your choice:").strip()

    if choice == "1":
        x = get_float("Enter a value:")
        print(f"\nValue = {x}")
        print(f"math.ceil({x}) = {math.ceil(x)}")
        print(f"math.floor({x}) = {math.floor(x)}")
        print(f"math.trunc({x}) = {math.trunc(x)}")

    elif choice == "2":
        n = get_int("Enter a non-negative integer:")
        try:
            print(f"\nmath.factorial({n}) = {math.factorial(n)}")
        except ValueError:
            print("factorial(x) needs a non-negative integer. Skipped.")

    elif choice == "3":
        a = get_float("Enter the length of side a:")
        b = get_float("Enter the length of side b:")
        print(f"\nmath.hypot({a}, {b}) = {math.hypot(a, b)}")

    elif choice == "0":
        return

    else:
        print("\nInvalid Choice.")

    pause()

#SECTION5
def random_menu():
    print_header("THE RANDOM MODULE")
    print("""1. Set a seed (so results can be repeated)
2. Generate a number with randrange()
3. Generate a number with randint()
4. Pick a random item from a list with choice()
5. Draw several UNIQUE items from a list with sample() (like a lottery)
0. Back to Main Menu
""")

    choice = safe_input("Enter your choice:").strip()

    if choice == "1":
        seed_val = get_int("Enter a seed value (an integer):")
        random.seed(seed_val)
        print(f"\nSeed set to {seed_val}. Random results will now repeat "
              "each time you use this same seed.")

    elif choice == "2":
        start = get_int("Enter the start of the range:")
        stop = get_int("Enter the stop of the range (exclusive):")
        try:
            print(f"\nrandom.randrange({start}, {stop}) = {random.randrange(start, stop)}")
        except ValueError:
            print("Invalid range. Make sure start < stop. Skipped.")

    elif choice == "3":
        low = get_int("Enter the lowest possible value:")
        high = get_int("Enter the highest possible value:")
        try:
            print(f"\nrandom.randint({low}, {high}) = {random.randint(low, high)}")
        except ValueError:
            print("Invalid range. Make sure low <= high. Skipped.")

    elif choice == "4":
        raw = safe_input("Enter a list of items separated by commas:")
        items = [item.strip() for item in raw.split(",") if item.strip()]
        if not items:
            print("\nNo items entered. Skipped.")
        else:
            print(f"\nrandom.choice({items}) = {random.choice(items)}")

    elif choice == "5":
        raw = safe_input("Enter a list of items separated by commas:")
        items = [item.strip() for item in raw.split(",") if item.strip()]
        k = get_int("How many UNIQUE items do you want to draw?")
        try:
            print(f"\nrandom.sample({items}, {k}) = {random.sample(items, k)}")
        except ValueError:
            print("Sample size can't be larger than the number of items. Skipped.")

    elif choice == "0":
        return

    else:
        print("\nInvalid Choice.")

    pause()


def main_menu():
    while True:
        print_header("PYTHON MATH MODULE EXPLORER")
        print("""1. Trigonometric (circular) functions
2. Hyperbolic functions
3. Exponentiation and logarithm functions
4. General-purpose math functions
5. The random module
6. Run the constants
0. Quit
""")
        choice = safe_input("Enter your choice:").strip()

        if choice == "1":
            trig_menu()

        elif choice == "2":
            hyperbolic_menu()

        elif choice == "3":
            exponent_menu()

        elif choice == "4":
            general_menu()

        elif choice == "5":
            random_menu()

        elif choice == "6":
            demo_constants()
            pause()

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid Choice.")


if __name__ == "__main__":
    main_menu()