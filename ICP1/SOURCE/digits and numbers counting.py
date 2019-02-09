data=input("enter a string")   # Taking a string from user
letters=numbers=0              # Initially taking letters and numbers as zero
for i in data:
    if i.isdigit():            # checking whether it is a digit or not using isdigit
        numbers =numbers+1     # storing that digit in the numeric
    elif i.isalpha():          # checking whether it is a alphabet or not using isalpha
        letters =letters+1     # storing that word in the letters

print("the number of numbers ",numbers)                # printing numbers
print("the number of letters",letters)                 # printing letters