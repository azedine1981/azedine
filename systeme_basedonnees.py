#mini sytème de base de données

def consultation():
    while 1:
        nom=input("Entrez le nom (ou <enter> pour terminer)")
        if nom=="":
            break
        if nom in dico:
            item=dico[nom]
            age,taille=item[0],item[1]
            print("Nom:{0}-âge: {1} ans - taille:{2}m.".\format(nom,age,taille))
        else:
            print("***nom inconnu!***)
def remplissage():
    pass
