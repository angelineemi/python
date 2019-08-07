a=1
b=0
c=3
try:
    print(a*c/b)
except(ZeroDivisionError, IOError,ArithmeticError) as e:
    print("An error has occured")
