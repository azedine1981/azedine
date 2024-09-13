from tkinter import *
def fct():
    can.coords(oval1,100,100,150,150)
    can.coords(ligne1,10,150,100,200)
    can.coords(carre,300,300,350,350)

root=Tk()
root.geometry('600x600')
root.title("les coordonnées d'un items dans un canvas")
larg=400
long=400
#création de widgets
can=Canvas(root,width=larg,height=long,bg='yellow')
can.pack(padx=3,pady=5)

oval1=can.create_oval(50,50,100,100,fill='red')
ligne1=can.create_line(10,0,100,50,fill='blue')
carre=can.create_rectangle(200,250,300,160,fill='purple')




bt=Button(root,text="Changer la position",command=fct)
bt.pack()




root.mainloop()
