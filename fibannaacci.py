def fib_1(num):
    num_1 = 0
    num_2 = 1

    if num == 0:
        print("incorrect input")
    elif num == 1:
        print("fibanacci series: ", num_1)
    else:
        print("fibanncci series = ", end="")
        for i in range(2, num+1):
            print(num_1, end=" ")
            res = num_1 + num_2
            num_1 = num_2
            num_2 = res
        print(num_1)
        print("\n", num, "th fib. number is : ", num_1)


def fib_2(num):
    add = 0
    if num <= 0:
        print("incorrect input")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        fib = fib_2(num-1) + fib_2(num-2)
        print(fib)
        return fib


num = 10
a= fib_1(10)
# print(a)
