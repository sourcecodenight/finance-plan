# this function is to calculate in hand salary against a package.
# this function will ask for few parameters and then will give in hand salary
# this function also have plan to use the data given by users and will give the
# option to calculate by selecting the company name only
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
#now rewrite function by changing the var to input functions