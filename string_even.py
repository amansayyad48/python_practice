def string_even(string, n):
    print("Original string is: ", string)
    print("Printing only even index chars")
    new_string = string[n:]
    print("new string: ", new_string)
    x = list(string)
    y = []
    for i in x[0::2]:
        print(i)
        y.append(i)
    print(str(y))


s = str(input("give the string: ",))
num = int(input("give number to slice from string: ",))
if num > len(s):
    num = int(input(f"give number less than {len(s)}: ",))
string_even(s, num)
