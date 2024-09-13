from tkinter import *
from tkinter import ttk
app=Tk()
app.geometry('500x400')
app.configure(bg='aqua')
app.title("Une abse de données tkinter")
#créer un arbre
arbre=ttk.Treeview(app)
#céer les colonnes =cet arbre
arbre['columns']=('#0','name','city')
#le formatage des colonnes
arbre.column('#0',width=100,anchor=W)
arbre.column('name',width=100,anchor=CENTER)
arbre.column('city',width=100,anchor=W)
#créer les en-têtes
arbre.heading('#0',text='ID',anchor=W)
arbre.heading('name',text='Nom',anchor=CENTER)
arbre.heading('city',text='Ville',anchor=W)

#afficher la table
arbre.pack(padx=5,pady=3)
#Ajouter des insertions
arbre.insert(parent='',index='end',iid=0,text="parent",values=('0','azedine','Agadir'))



app.mainloop()
