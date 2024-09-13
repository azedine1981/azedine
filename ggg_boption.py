from tkinter import *
racine=Tk()
racine.geometry('300x300')
racine.title("Manipuler les boutons radios")
#la création des boutons

l=["1ère année","2 ème année","3 ème année"]
for i in range(len(l)):
    bt=Radiobutton(racine,text=l[i],variable=StringVar()).pack(anchor="w")



racine.update()
racine.mainloop()
