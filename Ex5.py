def Calcul(a,b,op):
    if  op=='+':
        print("L'addition :",a,"+",b,"= ",a+b)
    if  op=="-":
        print("La soustraction :",a,"-",b,"= ",a-b)
    if  op=='*':
        print("La multiplication :",a,"*",b,"= ",a*b)
    if op=='/':
        print("La division :",a,"/",b,"= ",a/b)

a=int(input("Donner la valeur de a :"))
b=int(input("Donner la valeur de b :"))
op=input("Sasir l'operation correspondante (+,-,*,/) :")
Calcul(a,b,op)