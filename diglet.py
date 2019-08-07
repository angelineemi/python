str1=str(input("Enter a string: "))
digits=0
letters=0
for dl in str1:
    if dl.isdigit():
        digits+=1
    elif dl.isalpha():
        letters+=1
    else:
        pass
print("The number of letters are: ",letters)
print("The number of digits are: ",digits)
