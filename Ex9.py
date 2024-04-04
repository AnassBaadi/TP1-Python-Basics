def numParfait(n):
    s=0;
    for i in range(1,n):
        if (n%i==0):
            s+=i
    if s==n:
        print(n," est un Nombre Parfait !")
    else:
        print(n," n'est pas un Nombre Parfait !")
num=int(input("Donner un nombre a verifier s'il est parfait ou pas :"))
numParfait(num)