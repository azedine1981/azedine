from tkinter import *
app=Tk()
app.geometry('400x400')
app.title('widgets en boucle')

liste=['un','deux','trois','quatre']

cadre=Frame(app,width=100,height=200,relief="raised",borderwidth=3).pack(side=LEFT)

for i in liste:
    lbl=Label(cadre,text=str(i),bg='purple').pack()

app.mainloop()
