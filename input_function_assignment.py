#___________Number Ones____________
def ones(x):
    if x == 0:
        return ""
    elif x == 1:
        return "One"
    elif x == 2:
        return "Two"
    elif x == 3:
        return "Three"
    elif x == 4:
        return "Four"
    elif x == 5:
        return "Five"
    elif x == 6:
        return "Six"
    elif x == 7:
        return "Seven"
    elif x == 8:
        return "Eight"
    elif x == 9:
        return "Nine"

#___________Number Tens____________
def tens(x):
    if x == 10:
        return "Ten"
    elif x == 11:
        return "Eleven"
    elif x == 12:
        return "Twelve"
    elif x == 13:
        return "Thirteen"
    elif x == 14:
        return "Fourteen"
    elif x == 15:
        return "Fifteen"
    elif x == 16:
        return "Sixteen"
    elif x == 17:
        return "Seventeen"
    elif x == 18:
        return "Eighteen"
    elif x == 19:
        return "Nineteen"
    elif x >= 20:
        if x // 10 == 2:
            return "Twenty"
        elif x // 10 == 3:
            return "Thirty"
        elif x // 10 == 4:
            return "Forty"
        elif x // 10 == 5:
            return "Fifty"
        elif x // 10 == 6:
            return "Sixty"
        elif x // 10 == 7:
            return "Seventy"
        elif x // 10 == 8:
            return "Eighty"
        elif x // 10 == 9:
            return "Ninety"

#___________Number Hundreds____________
def hundreds(x):
    return ones(x) + " Hundred"

#___________Number Thousands____________
def thousands(x):
    return ones(x) + " Thousand"


num = int(input("Enter a number: "))

if num == 0:
    print("Zero")

elif num < 10:
    print(ones(num))

elif num < 20:
    print(tens(num))

elif num < 100:
    print(tens(num) + " " + ones(num % 10))

elif num < 1000:
    if num % 100 == 0:
        print(hundreds(num // 100))
    elif num % 100 < 20:
        print(hundreds(num // 100) + " " + tens(num % 100))
    else:
        print(hundreds(num // 100) + " " + tens(num % 100) + " " + ones(num % 10))

elif num < 10000:
    if num % 1000 == 0:
        print(thousands(num // 1000))
    elif num % 1000 < 10:
        print(thousands(num // 1000) + " " + ones(num % 1000))
    elif num % 1000 < 20:
        print(thousands(num // 1000) + " " + tens(num % 1000))
    elif num % 1000 < 100:
        print(thousands(num // 1000) + " " + tens(num % 1000) + " " + ones(num % 10))
    elif num % 100 == 0:
        print(thousands(num // 1000) + " " + hundreds((num % 1000) // 100))
    elif num % 100 < 20:
        print(thousands(num // 1000) + " " + hundreds((num % 1000) // 100) + " " + tens(num % 100))
    else:
        print(thousands(num // 1000) + " " + hundreds((num % 1000) // 100) + " " + tens(num % 100) + " " + ones(num % 10))