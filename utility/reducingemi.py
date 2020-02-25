# Formula for Bank EMI 
# EMI = [P x R x (1+R)^N]/[(1+R)^N-1]
# take R = R/1200 instead of R/12

print("Let's calculate your Bank's EMI!")
principal_amount = float(input("Enter your principal amount: "))
annual_rate_of_interest = float(input("Enter your annual rate of interest: "))
loan_tenure = int(input("Enter the number of months for which you seeking loan: "))
def loan_emi(P, R, N):
    return (P * R * ((1+R) ** N)/(((1+R) ** N)-1))
total_payable = 0
for i in range(loan_tenure):
    total_payable = total_payable + loan_emi(principal_amount-total_payable, annual_rate_of_interest/12, loan_tenure-i) 
    print(total_payable)

print(total_payable)
    