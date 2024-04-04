def somme10(n):
    s=0
    for i in range (n+1):
        s=s+10**i
    return s
pow=int(input("Donner la puissance :"))
print(somme10(pow))
