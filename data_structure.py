# sample_list = [11, 21, 10, 11, 40, 40, 50, 10, 11, 21]
#
# count_dict = dict()
#
# for i in sample_list:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
#
# print(count_dict)
#
# for i in count_dict:
#     if count_dict[i] > 2:
#         print(i, ":", count_dict[i])
list_a = ["a", "b", "c", "d", "e"]
list_b = ["f", "g", "h", "i", "j"]
list_a.pop(0)
list_a.insert(0, "a")
print(list_a)
list_a.append("a")
print(list_a.count("a"))
# g = len(list_a)
# list_c = list(list_a[i] + " " + list_b[i] for i in range(len(list_a)))
print(dict(i for i in zip(list_a, list_b)))
for i, y in zip(list_a, list_b[::-1]):
    print(i, y)
