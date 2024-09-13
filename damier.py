from tkinter import *

def lignes_verticales(c,nc,nl):
    x=0
    while x < nc*c:
        canevas.create_line(x,0,x,nl*c,width=1,fill='black')
        x += c

c = 40 # côté d'un carré
nl = 4 # nombre de lignes du damier
nc = 6 # nombre de colonnes

fen = Tk()
canevas = Canvas(fen, width=c*nc-3, height=c*nl-3, bg='white')
canevas.pack(side=TOP)

lignes_verticales(c,nc,nl)

fen.mainloop()
