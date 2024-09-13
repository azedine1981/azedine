from tkinter import *
def ajouter():
    for i in liste:
        lbox.insert(END,i)
def effacer():
    lbox.delet()
    
liste=['Orange','Fraise','Banane','Melon','raisin','Figue','grenade','pomme']
racine=Tk()
racine.geometry('300x500')
racine.title("la maîtrise de listbox")
#création des widgets principaux
lbox=Listbox(racine,width=10,height=20,selectbackground='blue')
lbox.pack()

bajout=Button(racine,text="Ajouter",bg='red',command=ajouter)
bajout.pack()

befface=Button(racine,text="Effacer",bg='red',command=effacer)
befface.pack()






racine.update()
racine.mainloop()
