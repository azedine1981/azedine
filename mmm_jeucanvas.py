from tkinter import *
def gauche(event):
    x=-5
    y=0
    can.move(carre,x,y)
def droit(event):
    x=+5
    y=0
    can.move(carre,x,y)
    
def haut(event):
    x=0
    y=-5
    can.move(carre,x,y)

    
def bas(event):
    x=0
    y=+5
    can.move(carre,x,y)
#-----------------------------------------------------------modifier les options items canvas-------------------------
def fct():
    can.itemconfigure(carre,fill="pink")



app=Tk()
app.title("jeu dans un canvas")
app.geometry('500x500')
app.configure(bg='aqua')
#les widgets

can=Canvas(app,width=400,height=400,bg='yellow')
can.pack()
texte=can.create_text(200,200,anchor='w',fill='blue',text="le jeu le plus dangereaux commmence!",font="50,bold",angle=45)
carre=can.create_rectangle(200,250,300,160,fill='purple')
balle=can.create_oval(50,50,100,100,fill='green')
#------------------------------------------------------------------------------------------------------------------------
can.after(1000,fct)

app.bind("<Left>",gauche)
app.bind("<Right>",droit)
app.bind("<Up>",haut)
app.bind("<Down>",bas)

app.update()

app.mainloop()
