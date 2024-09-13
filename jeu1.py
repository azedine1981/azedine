from tkinter import *
from tkinter.font import Font
#les fonctions qui gèrent les tâches
def sauter():
    pass

#la fenête principarle
racine=Tk()
racine.geometry('500x400')
racine.title("Commencer votre jeu")

fImage=PhotoImage(file='jeu.png')
can=Canvas(racine,width=100,height=100,bg='ivory')
can.pack(padx=5,pady=5)
can.create_image(150,100,image=fImage)
police=Font(size=12,weight='bold')
                 
b1=Button(racine,text='Sauter',font=police,bg='aqua',command=sauter)
b1.pack(SIDE=TOP,padx=5,pad=5)




racine.mainloop()
