def alphapat(n):
    num=65
    for i in range (0,n):
          for j in range (0,i+1):
              charac=chr(num)
              print(charac ,end=" ")
              num=num+1
          print("\r")
n=int(input("Enter a number: "))
alphapat(n)
    
