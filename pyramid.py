num = 50
m = (num * 2)-4
for i in range(0, num):
    for j in range(m):
        print(end=" ")
    m = m-1
    for j in range(i):
        # print(3*"\t")
        print("*", end=" ")
    print("\t")

n = (num*2)-8
for i in range(0, 30):
    for j in range(n):
        print(end=" ")
    print(8*"*")


