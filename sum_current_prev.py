def sum_curr_prev(range_number):
    sum = 0
    previous = 0
    addition = 0
    for i in range(range_number+1):
        sum += i
        addition = i + previous
        print(f"sum of current number {i} and previous number {previous} is : ", addition)
        previous = i

    print(f"sum of all number for range {range_number} : ", sum)


Range_number = int(input("Give the range number: ",))
sum_curr_prev(Range_number)