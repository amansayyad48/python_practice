list_1 = [12, 13, 14, 15, 16, 17]
list_2 = [22, 23, 24, 25, 26, 27]

new_list = []

for i in list_1[:]:
    if i % 2 == 1:
        new_list.append(i)

for i in list_2[:]:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)

