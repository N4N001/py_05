def prvniposledni(cisla):
    if cisla[0]==cisla[len(cisla)-1]:
        print("TRUE")
    else:
        print("FALSE")
cisla=input("Zadejte čísla oddělená čárkou: ")
cisla=cisla.split(",")
cisla=[int(x) for x in cisla]
prvniposledni(cisla)
input("Stiskni klávesu ENTER pro ukončení programu")