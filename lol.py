list1=["lydia","princy","sunethra"]
print(list1)
list1.append("ange")
list1.append("freeda")
list1.remove("lydia")
list1.insert(0,"kathy")
print(list1)
for i in range(0,len(list1)):
    print("patient",i+1,"is",list1[i])
