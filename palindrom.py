org_num = int(input("original number: ",))
reverse_num = 0
number = org_num
while number > 0:
    reminder = number % 10
    reverse_num = (reverse_num*10) + reminder
    number = number // 10

if org_num == reverse_num:
    print(f"Yes, {org_num} is palindrome number.")
else:
    print(org_num, "it's not palindrome number.")

print(org_num//10)
