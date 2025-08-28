"""emi = (p*r*(1+r)^n) /((1+r)^n-1)

p=loan amount
r=monthly interest rate(annual_rate/(12*100))
n=loan tenure in months (6*12)

"""

loan_amount = int(input("enter loan amount")) #600000

interest_rate = int(input("enter interest rate")) #9

loan_tenure = int(input("enter tenure")) #6

p = loan_amount

r = interest_rate/(12*100)

n = loan_tenure*12

emi = ( p*r*(1+r)**n) /((1+r)**n-1 )

total_payable_amount = emi * n 

total_interest_payable = total_payable_amount - loan_amount

print("emi=",round(emi,2),"total payable amount",round(total_payable_amoun),"total interest",round(total_interest_payable))


