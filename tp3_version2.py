from tkinter import *
def fct(event):
    t=event.keysystem
def g(event):
    pass

root=Tk()
root.geometry('600x500')
root.title("L'apllication de la fin du mois Avril")
side=200

mon_menu=Menu(root)
root.config(Menu=mon_menu)
#un premier menu
fichier=Menu(mon_menu,tearoff=0)
#un deuxième menu

cnv=Canvas(root,widt=side,height=200,bg='olive')
cnv.pack(padx=10,pady=10)

lbl=Label(root,text='*********',bg='ivory')
lbl.pack()

btn=Button(root,text="commencer l'essaie", bg='red',command=fct)
btn.pack()


root.mainloop()
