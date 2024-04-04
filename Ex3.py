def Conversion(T):
    h=T/3600
    m=(T%3600)/60
    s=(T%3600)%60
    print("T=",T,"secondes   =",int(h)," Heures ",int(m),"Minutes ",int(s)," Secondes")

T=int(input("Entrez le temps en secondes :"))
Conversion(T)

#Remarque: casting sur ligne de creation de fonctionne pas