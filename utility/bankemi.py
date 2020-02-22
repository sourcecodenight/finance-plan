# Formula for Bank EMI 
# EMI = [P x R x (1+R)^N]/[(1+R)^N-1]

print("Let's calculate your Bank's EMI!")
principal_amount = float(input("Enter your principal amount: "))
annual_rate_of_interest = float(input("Enter your annual rate of interest: "))
loan_tenure = float(input("Enter the number of months for which you seeking loan: "))
monthly_rate_of_interest = annual_rate_of_interest/12
monthly_emi = ((principal_amount * monthly_rate_of_interest) * ((1 + monthly_rate_of_interest) ** loan_tenure))/((1 + monthly_rate_of_interest) ** loan_tenure -1)
print("Your monthly EMI is : "+ str(monthly_emi))