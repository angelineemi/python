a=[1,2,3,4]
try:
    print(a[5])
except(IndexError):
    print("No element at the specified index")
