from tkinter import *
def f(event):
    t=event.keysym
    print("la touche préssée:",t)

def g(event):
    x=event.x
    y=event.y
    print("la position de votre souris:",x,y)

fenetre=Tk()
fenetre.geometry('400x400')
fenetre.bind('<Key>',f)
fenetre.bind('<Motion>',g)
fenetre.mainloop()
