from tkinter import Canvas,Tk
def mv():
    pass

fen=Tk()
fen.geometry('600x600')
can=Canvas(fen,width=400,height=400,bg='yellow')
can.pack(padx=5,pady=5)
balle=can.create_oval((100,150),(160,300),fill='light blue',outline='red')

btn=Button(fen,text='Animer',command=mv).pack(padx=3,pady=5)


fen.mainloop()
