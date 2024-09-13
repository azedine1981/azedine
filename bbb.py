from tkinter import *
racine=Tk()
racine.title("la fenêtre principale")
racine.geometry('500x600')
li=['Accueil','Commencer un nouveau jeu','sauvegarder le résultat','quiter']

can=Canvas(racine,width=300,height=300,bg='red')
can.pack()
#créer certaines canvas items 
ligne=can.create_line(0,0,200,200,width=3)
cercle=can.create_oval(250,250,300,300,width=2,fill='green')

#créer une zone de texte
entree=Entry(racine,text='Entrez votre nom:')
entree.pack()
#création d'un conteneur frame
frame1=Frame(racine,width=300,height=50,bg="blue")
frame1.pack(side=BOTTOM)

for l in li:
    bt=Button(frame1)
    bt['text']=l
    bt.pack(side=TOP)



    
racine.mainloop()
