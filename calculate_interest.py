amount = float(input("Enter amount: ",))
intrest = 0

if amount > 20000:
    intrest = (10000*0.1)+(amount-20000)*0.2

elif amount > 10000:
    intrest = (amount-10000)*0.2

else:
    intrest = 0

print(intrest)

