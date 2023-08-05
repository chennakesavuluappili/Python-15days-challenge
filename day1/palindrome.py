string1=input("Enter the string : ")
string2=string1[::-1]
if string1.lower()==string2.lower():
    print("{0} is palindrome".format(string1))
else:
    print("{0} is not palindrome".format(string2))
