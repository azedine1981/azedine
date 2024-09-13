from tkinter import *
import sqlite3

valeur =StringVar()
    
def envoyer():
    with sqlite3.connect('abase.db') as connection:
    cur=connection.Cur()
    val=valeur.get()


    connection.close()

racine=Tk()
racine.geometry('600x600')
racine.title('Tester quelques widgets')
cadre=Frame(racine,width=400,height=400,bg='yellow',bd=10)
cadre.pack()

nom=Label(cadre,text="Nom",bg='olive')
nom.place(x=5,y=5)
entree_nom=Entry(cadre,width=30,textvariable=valeur))
entree_nom.place(x=40,y=5)

age=Label(cadre,text="Qu'il âge as-tu?",bg='olive')
age.place(x=5,y=40)
entree_age=Entry(cadre,width=30)
entree_age.place(x=40,y=40)

enregistrer=Button(racine,text="Envoyer les données",bg='ivory',command=envoyer)
enregistrer.pack()

quitter=Button(racine,text="Quitter",bg='ivory',command=racine.destroy)
quitter.pack()


racine.mainloop()
