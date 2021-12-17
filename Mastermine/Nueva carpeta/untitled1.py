# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 21:50:33 2021

@author: rodau
"""

from tkinter import *
ventana=Tk()
ventana.title("Mastermine")
ventana.geometry("405x720")
#p1 = PhotoImage(file ="punto 1.png")

def cambiar():
    ventana.configure(bg="darkgoldenrod4")
    Label(ventana,image=p1).grid(row=2, column=1,rowspan=1,pady=5)
    
b9=Button(ventana,command=lambda:cambiar())
b9.config(font="Arial 12",width="9",text=" Cambia ")
b9.grid(row=1,column=1,padx=30,pady=30)
#pv = PhotoImage(file ="vacio.png")
#Label(ventana,image=pv).grid(row=2, column=1,rowspan=1,pady=5)

ventana.mainloop()
