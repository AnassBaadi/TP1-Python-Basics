def ordreCroissant(T):
    n=len(T)
    for i in range(n):
        if  i !=n-1 and (T[i]>T[i+1]) : 
            print("Ce tableau n'est pas trie d'ordre croissant !")
            return 1;
    print("Ce tableau est trie d'ordre croissant !")
n=int(input("Donner la longueur du Tableau :"))
Tab=[]
for i in range(n):
    print("Entrez l'element:",i)
    Tab.append(int(input()))
ordreCroissant(Tab)

# Remarque : if (T[i]>T[i+1]) and i !=n-1  : ne fonctionne pas il faut changer l'ordre 