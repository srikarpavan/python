n=int(input("Total number of values"))
x=(input("values in the list"))
sum=0.0
list=x.split()
for num in list:
    sum=sum+int(num)
print("sum of the values:",sum)
print("Average of the total value is:",sum/n)