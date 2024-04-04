def moy(n1,n2,n3):
    return (n1+n2+n3)/3
    
n1=float(input("Entrer la 1ere note :"))
n2=float(input("Entrer la 2eme note :"))
n3=float(input("Entrer la 3eme note :"))
if(n1 or n2 or n3 )> 20: #Remarque: 20 doit etre au dehors des parentheses
    print("Note Superieur de 20")
else :
    moy=moy(n1,n2,n3)
    if (moy>=16):
        print("Tres Bien")
        print(moy)
    elif (moy>=14):
        print("Bien")
        print(moy)
    elif(moy>=12):
        print("Assez Bien")
        print(moy)
    elif (moy>=10):
        print("Passable")
        print(moy)
    else:
        print("Insuffisant")
        print(moy)