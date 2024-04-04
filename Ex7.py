def nsomme(n):
    s=0
    for i in range(n+1):
         s+=i**2
    print(s," = ")
    for i in range(1,n+1):
         s+=i**2
         if i==n:
              print(i**2)
              break
         print(i**2,"+") 
nsomme(3)
         