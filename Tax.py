#This program calculates Tax.
#Last Modified: 20 Decemeber 2014
#Created By: Zehra Punjwani

#INPUTS
grossSalary = float(input("Please enter the employee's gross salary: "))
taxCode = str(raw_input("Please enter the employee's tax code: ")).upper()

#CONSTANTS
EMPLOYEE_PENSION_CONTRIBUTION = 0.05 * grossSalary
EMPLOYER_PENSION_CONTRIBUTION = 0.075 * grossSalary
LOWER_BOUND = 0.09
UPPER_BOUND = 0.49

3200

#SECTION B
pensionTotal = EMPLOYEE_PENSION_CONTRIBUTION + EMPLOYER_PENSION_CONTRIBUTION
salaryAfterPension = grossSalary - EMPLOYEE_PENSION_CONTRIBUTION

#SECTION C
taxDigits = int(taxCode[:4])
taxLetter = taxCode[4:]
taxAllowance = 0
digitAllowance = taxDigits * 10
if taxLetter == "Z":
    taxAllowance = digitAllowance + 1000
else :
    taxAllowance = digitAllowance

#SECTION D & E
tax = 0
lowerTax = 0
upperTax = 0
if salaryAfterPension < taxAllowance:
	taxableSalary = 0
else:
	taxableSalary = salaryAfterPension - taxAllowance
	
if taxAllowance >= grossSalary:
    tax = 0
elif taxAllowance < grossSalary:
    if  taxableSalary <= 40000:
        lowerTax = taxableSalary * LOWER_BOUND
    else:
        lowerTax = 40000 * LOWER_BOUND
        upperTax =(taxableSalary - 40000) * UPPER_BOUND
    tax = upperTax + lowerTax
        
netSalary = salaryAfterPension - tax

print("*****************************************************")
print("Tax Code: ", taxCode)
print("Gross Salary: %.2f" %grossSalary)
print("*****************************************************")
print("Employee's Pension Contribution:%.2f" %EMPLOYEE_PENSION_CONTRIBUTION)
print("Employer's Pension Contribution: %.2f" %EMPLOYER_PENSION_CONTRIBUTION)
print("Total Pension Contribution: %.2f" %pensionTotal)
print("Gross Salary After Pension: %.2f" %salaryAfterPension) 
print("*****************************************************")
print("Personal Allowance: %.2f" %taxAllowance)
print("*****************************************************")
print("Taxable Salary: %.2f" %taxableSalary)
print("Lower Tax Amount: %.2f" %lowerTax)
print("Upper Tax Amount %.2f" %upperTax)
print("Total Tax Amount %.2f" %tax)
print("*****************************************************")
print("Net Salary: %.2f" %netSalary)
