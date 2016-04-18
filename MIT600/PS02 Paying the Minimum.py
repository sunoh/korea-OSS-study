balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

numMonth = 12
totalPaid = 0

for month in range(numMonth):
    print 'Month: ' + str(month+1)
    print 'Minimum monthly payment: ' + str(round(balance*0.04,2))
    totalPaid += balance*0.04
    balance = balance - (balance*0.04)
    balance = balance + (balance * annualInterestRate / 12)
    print 'Remaining balance: ' + str(round(balance,2))

print 'Total paid: '+ str(round(totalPaid,2))
print 'Remaining balance: ' + str(round(balance,2))

    