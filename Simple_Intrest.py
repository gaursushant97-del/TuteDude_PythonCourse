principal=float(input("Enter the principal amount:"))
rate=(float(input("Enter the rate of intrest charged (In Percentage only):")) / 100)
time=float(input("Enter the time period (in years only):"))
SI=principal*rate*time
print("your total simple interest is",round(SI,2))

print("Total amount you have to pay is",round((principal+SI),2))
Compound=int(input("Enter the compounding rate:"))
CI=principal * (1+rate) ** (time*Compound) - principal
print("your total compound interest is",round(CI,2))
print("Total amount you have to pay is",round((principal+CI),2))

print("your monthly Emi Stands at", round((principal+CI),2)//(time*12))


