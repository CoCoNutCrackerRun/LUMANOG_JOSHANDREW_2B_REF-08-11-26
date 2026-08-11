name = str("Josh Lumanog")
print (name)

age = int(20)
print(age)

lbs = float(110.231)
print(lbs)

mode1 = True
mode2 = False

print(mode1)
print(mode2)


data1 = input("Enter your name: ")
data2 = int(input("Enter your age: "))
data3 = float(input("Enter your weight in lbs: "))
data4 = input("Enter your mood (Happy or Sad): ")
if data4 == "Happy":
    print(f"Hello, {data1}! You are {data2} years old, and weigh {data3} in lbs. You are Happy")
else:
    print(f"Hello, {data1}! You are {data2} years old, and weigh {data3} in lbs. You are Sad.")