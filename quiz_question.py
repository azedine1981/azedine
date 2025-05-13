#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:38:32 2025

@author: rah1981
"""

from tkinter import *
dic_question={'question1':'reponse1', 'question2':'reponse2'}
def valider():
    '''une foction pour soumettre les changements'''
    pass
def suivant():
    '''une fonction pour passer à la question suivante'''
    pass
root=Tk()
root.geometry('600x600')
root.title("Quiz question")
#création du widget canvas et les images
ph=PhotoImage(file='/home/rah1981/ordi.png')
lbl=Label(root,image=ph,width=80,height=80)
lbl.pack()

#création d'autres widgets
btn_valider=Button(root,text="Valider",command=valider)
btn_valider.pack()
btn_suivant=Button(root,text="Suivant",command=suivant)
btn_suivant.pack()
btn_quitter=Button(root,text="Quitter",command=root.destroy)
btn_quitter.pack()



root.mainloop()
