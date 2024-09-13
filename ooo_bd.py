from tkinter import *
import sqlite3

def enregistrer():
    nom=stringVar(entr1.get())
    ville=strinVar(entr2.get())
    conn=sqlite3.connect("abase.db")
    cur=conn.cursor()
    cur.execute('INSERT INTO t3(Nom,Ville) VALUES(nom,ville)')
    conn.commit()
    cur.close()
    conn.close()



if __name__ == "__main__":
    app=Tk()
    app.title("ça se relie avec une base de données")
    app.geometry('500x500')
    
    global entr1
    global entr2
    lbl1=Label(app,text="Nom",bg='ivory')
    lbl1.place(x=5,y=5)
    entr1=Entry(app)
    entr1.place(x=50,y=5)
    lbl2=Label(app,text="Ville",bg='ivory')
    lbl2.place(x=5,y=40)
    entr2=Entry(app)
    entr2.place(x=50,y=40)
    btn=Button(app,text="Sauvegarder les données",bg='aqua',command=enregistrer)
    btn.place(x=50,y=100)

    app.mainloop()
