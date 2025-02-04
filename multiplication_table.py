num_t = int(input("enter number for table: ",))
for i in range(1, num_t+1):
    print("table of ", i)
    for j in range(1,11):
        print(j*i, end=" ")
    print("\n")


# def numbers(*args):
#     print(type(args))
#     args = list(args)
#     args.append(40)
#     print(args)
#     print(type(args))
#
#
# numbers(50, 60, 70, 80)
