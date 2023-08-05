list1=list(map(int,input("Enter the list of values: ").split()))
s=0
for i in range(len(list1)):
    if list1[i]>0:
        s+=list1[i]
print("Sum of positive values is: ",s)