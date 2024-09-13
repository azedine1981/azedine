from tkinter import *

def ouvrir():
    print("bonjour tout le monde")
def enregistrer():
    print("avez-vous un fichier à enregistrer")
def enregistrersous():
    print("il faut choisir un nom à votre fichier")
def quitter():
    root.quit
root=Tk()
root.geometry('500x500')
root.title("Créer des menus")
# cération d'une barre de menus
barmenu=Menu(root)
root.config(menu=barmenu)
#créer le nemu fichier
menufichier=Menu(barmenu,tearoff=0)
menuedition=Menu(barmenu,tearoff=0)
menuaffichage=Menu(barmenu,tearoff=0)
#ajouter des 
barmenu.add_cascade(label="Fichier",menu=menufichier)
barmenu.add_cascade(label="Edition",menu=menuedition)
barmenu.add_cascade(label="Affichage",menu=menuaffichage)

#ajout des commandes au menu fichier
menufichier.add_command(label="Ouvrir",command=ouvrir)
menufichier.add_command(label="Enregistrer",command=enregistrer)
menufichier.add_command(label="Enregistrer sous",command=enregistrersous)
menufichier.add_command(label="Quitter",command=quitter)

#ajout des commandes au menu édition

menuedition.add_command(label="Copier")
menuedition.add_command(label="Couper")
menuedition.add_command(label="Coller")

#ajout de commndes au menu affichage
menuaffichage.add_command(label="Paramètres d'affichage")
menuaffichage.add_command(label="Zoom")




root.update()

root.mainloop()
