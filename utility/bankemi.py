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
monthly_emi = round(monthly_emi, 2)
total_interest = round(monthly_emi * loan_tenure - principal_amount, 2)
print("Your monthly EMI is : "+ str(monthly_emi))
print("You are paying a total interest of : INR "+ str(total_interest))
print("Principal Amount INR : "+ str(round(principal_amount,2)))
print("Total repay amount INR : "+ str(round(monthly_emi * loan_tenure,2)))
print("You are paying : INR "+ str(round((monthly_emi * loan_tenure - principal_amount)/loan_tenure,2))+ "per month as interest!!")