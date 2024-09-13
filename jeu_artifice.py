from tkinter import *
app=Tk()
app.title("Feu d'atifice")
app.geometry('500x500')
app.configure(bg='aqua')
#les fonctions
def fete():
    can.itemconfigure(ligne1,fill="red")
    can.itemconfigure(ligne2,fill="chocolate")
    can.itemconfigure(ligne3,fill="silver")
    can.itemconfigure(ligne4,fill="lavender")
def animer(event):
    pass

#les widgets
can=Canvas(app,width=200,height=200,bg='yellow')
can.pack()
btn=Button(app,text="Commencer le jeu",bg='ivory',command=animer)
btn.pack()
#les lignes
ligne1=can.create_line(100,100,100,5,fill='purple',width=4)
ligne2=can.create_line(100,100,195,100,fill='cyan',width=4)
ligne3=can.create_line(100,100,100,195,fill='magenta',width=4)
ligne4=can.create_line(100,100,5,100,fill='orange',width=4)


can.after(1000,fete)

app.update()
app.mainloop()
