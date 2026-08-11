my_list = []

for i in range(1,10):
    my_list.append(i)

print("Original List: ", (my_list))
print("Length of list: ", len(my_list))

y = 1
x = 0

while x < len(my_list):
    if my_list.count(my_list[x]) > 1:
        del my_list[x]
    else:
        y = y + 1
        x += 1

print("The list with unique elements only.")
print(my_list)