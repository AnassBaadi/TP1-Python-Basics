def impot(age,s):
    if(s=="h" and age>20):      #if (s=='h' and age>20) or (s=='f' and 18<=age<=35):
        print("Vous devez payez l'impot")
    elif s=='f' and age>18:
        if age<35:
            print("Vous devez payez l'impot")
        else:
            print("Pas de frais d'impot !")
    else:
        print("Pas de frais d'impot !")
AGE=int(input("Veuillez saisir votre Age :"))
SEX=input("Veuillez Saisir votre sex(h pour homme | f pour femme) :")
impot(AGE,SEX)