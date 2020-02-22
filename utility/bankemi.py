# Formula for Bank EMI 
# EMI = [P x R x (1+R)^N]/[(1+R)^N-1]
# take R = R/1200 instead of R/12

print("Let's calculate your Bank's EMI!")
principal_amount = float(input("Enter your principal amount: "))
annual_rate_of_interest = float(input("Enter your annual rate of interest: "))
loan_tenure = float(input("Enter the number of months for which you seeking loan: "))
monthly_rate_of_interest = annual_rate_of_interest/1200
temp_var = 1 + monthly_rate_of_interest
monthly_emi = principal_amount * monthly_rate_of_interest * ((temp_var**loan_tenure)/((temp_var**loan_tenure)-1))
print("Your monthly EMI is : "+ str(monthly_emi))