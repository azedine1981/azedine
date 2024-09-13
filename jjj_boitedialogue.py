from tkinter import *
from tkinter import filedialog

def ouvrir():
    f=filedialog.askopenfilename(title="Ouvrir un fichier",filetypes=[('fichier python','.py')])

def enregistrer():
    e=filedialog.asksaveasfile(title="Enregistrer-sous",filetypes=[('fichier texte','.txt')])
    
app=Tk()
app.title("une fenêtre avec boîte de dialogue")
app.geometry('300x300')
#widgets
btn_e=Button(app,text="Enregistrer-sous",command=enregistrer).pack()
btn_o=Button(app,text="Ouvrir",command=ouvrir).pack()


app.update()
app.mainloop()
