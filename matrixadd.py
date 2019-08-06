a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[1,2,3],
   [4,5,6],
   [7,8,9]]
add=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(3):
    for j in range(3):
        add[i][j]=a[i][j]+b[i][j]
        for r in add:
            print(r)
     
        
