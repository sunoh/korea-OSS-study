balance = 999999
annualInterestRate = 0.18

monthlyPayment = 0

numMonth = 12
remaining = balance

lb = balance / 12
ub = balance * (((1+(annualInterestRate /12))**12) / 12)

while True:
    remaining = balance
    monthlyPayment = (lb+ub)/2.0
    for month in range(numMonth-1):
        remaining -= monthlyPayment
        remaining += (remaining * annualInterestRate / 12)
    remaining -= monthlyPayment
    if round(remaining,2) > 0:
        lb = monthlyPayment
    elif round(remaining,2) < 0:
        ub = monthlyPayment
    elif round(remaining,2) == 0:
        break
        
print 'Lowest Payment: ' + str(round(monthlyPayment,2))