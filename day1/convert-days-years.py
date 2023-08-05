number=int(input("Enter the value : "))
years=round(number/365)
weeks=round((number%365)/7)
days=(number%365)%7
print("Number of years : {0}\nNumber of Weeks : {1}\nNumber of Days is : {2}".format(years,weeks,days))