import math

def eq2deg(a,b,c):
    delta=b**2-4*a*c
    if delta>0:
        x1=(-b+math.sqrt(delta))/2*a
        x2=(-b-math.sqrt(delta))/2*a
        print("Il existe deux solutions x1 =",x1, " et " ,x2)
    elif delta==0:
         x=-b/2*a
         print("Il existe une seul solution x=",x)
    else:
        print("Pas de Solutions Reels !") 
a=int(input("Donner la valeur de a :"))
b=int(input("Donner la valeur de b :"))
c=int(input("Donner la valeur de c :"))
eq2deg(a,b,c)

#Remarques : sqrt necessite une biblio ? et aussi print(f,"") ne fonctionne pas