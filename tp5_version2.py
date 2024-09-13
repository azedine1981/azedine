from tkinter import *
def fct():
    variable=StingVar()

racine=Tk()
racine.geometry('300x400')
lbl.set('6')
lbl=Label(racine,bg="ivory",height=5,width=40).pack(padx=3,pady=4)
comm=Button(racine,text="+",textvariable=variable,command=fct).pack()

racine.mainloop()
