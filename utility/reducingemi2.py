# next month principal
principal = float(input("Enter the principal amount: "))
tenure = int(input("Loan tenure in months: "))
interestrate = float(input("Annual Interest rate: "))
monthlyrate = interestrate/1200
accounted_principal = principal
for i in range(tenure):
    accounted_principal = accounted_principal (1+monthlyrate)
