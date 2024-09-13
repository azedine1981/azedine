from tkinter import *
racine=Tk()
racine.title("la fenêtre principale")
racine.geometry('500x600')

e1=Entry(racine,width=50,bg='yellow')
e1.pack()
e2=Entry(racine,text='Ville')
e2.pack()
e3=Entry(racine,text='âge')
e3.pack()
e4=Entry(racine,text='Adresse Email')
e4.pack()

racine.mainloop()
