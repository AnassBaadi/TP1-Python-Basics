def Compteur10(n):
    print("La Methode For(Pour):")
    for i in range(n+1,n+11):
        print(i)
def Compt10While(n):
    print("La Methode While(Tant que)")
    i=n+1
    while(i<=n+10):
        print(i)
        i+=1
num=int(input("Donner un entier :"))
Compteur10(num)
print("******************")
Compt10While(num)