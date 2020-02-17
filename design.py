#Retirement plan function is aimed to provide backtracking function for EMI calculation at a retirement age.
# Arguments : Monthly income post retirement, Retirement date, Saving plan interest annually
# Return: Monthly saving
def retirementPlan(incomePostRetirement, retirementDate, interestRate):
    #Do Calculation here
    return 0
def inHandSalary(CTC, variable, PF):
    tax = .1
    providentFund = CTC * PF/100
    variableAmount = CTC * variable/100
    taxDeduction = (CTC - variableAmount - providentFund) * tax
    salaryInHand = (CTC - providentFund - variableAmount - taxDeduction)
    return salaryInHand

if __name__ == "__main__":
    salary = inHandSalary(1800000, 7, 8)
    print("Monthly salary : ", salary/12)

