def same_number_addition(num):
    for i in range(1, num +1):
        start = i
        res = 0
        print(start, end=" ")
        for j in range(0, num):
            res = res + start
            start = (start*10) + i
            # print(start)
            print("+", start, end=" ")
        print(f"== {res}")


def prime_number(start_no, end_no):
    for i in range(25, 51):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, " is prime number.")


def reverse(numb):
    res = 0
    while numb > 0:
        rev = numb % 10
        res = res*10 + rev
        # print(res)
        numb = numb // 10
    return res


start = 25
end = 50
prime_number(start, end)

num = 5
same_number_addition(num)
number = 521
print(reverse(number))



