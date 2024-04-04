def prodScalaire(P,Q,n):
    T=[]
    for i in range(n):
        T.append(P[i]*Q[i])
    return T
P=[1,7,4,2,6] # On peut utiliser input ici (meme code que Ex10.1 partie input) ! mais il faut meme nombre d'elements n
Q=[1,0,1,2,6]
T=prodScalaire(P,Q,5)
print(T)