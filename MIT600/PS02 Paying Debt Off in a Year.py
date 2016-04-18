balance = 3329
annualInterestRate = 0.2

monthlyPayment = 0

numMonth = 12
remaining = balance

while remaining > 0:
    remaining = balance
    monthlyPayment += 10
    for month in range(numMonth):
        remaining -= monthlyPayment
        if remaining <= 0:
            break
        remaining += (remaining * annualInterestRate / 12)

print 'Lowest Payment: ' + str(monthlyPayment)