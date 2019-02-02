data=input("enter a string")   # Taking a string from user
letters=numbers=0              # Initially taking letters and numbers as zero
for i in data:
    if i.isdigit():            # checking whether it is a digit or not
        numbers =numbers+1     # storing that digit in the numeric
    elif i.isalpha():          # checking whether it is a alphabet or not
        letters =letters+1     # storing that word in the letters

print(numbers)                 # printing numbers
print(letters)                 # printing letters