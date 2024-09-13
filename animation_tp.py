from tkinter import *
""" un test d'une annimation simple"""
def avance():
    x,y=x+dx,y+dy
def bas():
    pass
def haut():
    pass
def gauche():
    pass
def droite():
    pass
#------------------------------------------------------------------
app=Tk()
app.title("une animation simple")
app.geometry('500x500')
app.configure(bg='magenta')
#création des widgets
can=Canvas(app,width=300,height=300,bg='olive').pack(side=TOP)
balle=Create_oval(can,x,x+30,y,y+30,fill='red')

#--------------------------------------------------------------------
btn_bas=Button(app,text="Bas",command=bas).pack()
btn_haut=Button(app,text="Haut",command=haut).pack()
btn_gauche=Button(app,text="Gauche",command=gauche).pack()
btn_droit=Button(app,text="Droite",command=droite).pack()

#--------------------------------------------------------------------
#coordonnées utilisées d'une manière globale
x=10,y=10,dx=5,dy=5

app.update()
app.mainloop()
