def distinct(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False
print(distinct([1,2,3,4,5]))
print(distinct([2,3,3,4,5]))
