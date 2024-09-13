from tkinter import *
wi=Tk()
wi.geometry('400x400')
wi.title("Glissière et ascensseur")
wi.config(bg='yellow')
#création d'une glissière
gli=Scale(from_=0,to=100)
gli.pack()
#création d'un ascensseur
ascensseur=Scrollbar(choix)

#création d'une lisbox
li=['un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix']

for l in li:
    choix.insert(END,l)
choix.pack()

choix=Listbox(wi,command=choix.yview)
choix.pack(side=LEFT,expand=True,fill=Y)
choix.config(yscrollcommand=choix.set)


wi.update()
wi.mainloop()
