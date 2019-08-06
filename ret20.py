def sum_ret(x,y):
    num=x+y
    if num in range(15,20):
        return 20
    else:
        return num
print(sum_ret(4,5))
print(sum_ret(15,4))
