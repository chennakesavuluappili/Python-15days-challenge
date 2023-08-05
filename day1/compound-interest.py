principal_amount=float(input("enter the principal amount : "))
rate_of_interest=float(input("enter the rate of interest : "))
time=float(input("enter time period in years: "))
a=principal_amount*pow((1+rate_of_interest/100),time)
compound_interest=a-principal_amount
print(compound_interest)