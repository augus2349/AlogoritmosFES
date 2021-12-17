# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:55:05 2021

@author: rodau
"""

from tkinter import *
import random


ventana=Tk()
ventana.title("Mastermine")
ventana.geometry("450x800")
ventana.configure(bg="darkgoldenrod4")
tablero=Frame(ventana,bg="darkgoldenrod4")
tablero.configure(bd=15)
tablero.pack(fill="both")


bot1=Button(tablero,font="Arial 12",width="9",text=" INICIAR ",command=lambda:star())
bot2=Button(tablero,font="Arial 12",width="9",text=" VACIAR ",command=lambda:sup())
bot1.grid(row=22, column=6,columnspan=5,padx=10)
bot2.grid(row=23, column=6,columnspan=5,padx=10)
#imagenes
p1 = PhotoImage(file ="punto 1.png")
p2 = PhotoImage(file ="punto 2.png")
p3 = PhotoImage(file ="punto 3.png")
p4 = PhotoImage(file ="punto 4.png")
p5 = PhotoImage(file ="punto 5.png")
p6 = PhotoImage(file ="punto 6.png")
p7 = PhotoImage(file ="punto 7.png")
p8 = PhotoImage(file ="punto 8.png")
pv = PhotoImage(file ="Vacio.png")
check1=PhotoImage(file="check 1.png")
check2=PhotoImage(file="check 2.png")
check3=PhotoImage(file="check 3.png")
checkv=PhotoImage(file="check v.png")
pres=PhotoImage(file="res.png")
#opciones
Label(tablero,image=p5).grid(row=23, column=2,rowspan=1)
Label(tablero,image=p6).grid(row=23, column=3,rowspan=1)
Label(tablero,image=p7).grid(row=23, column=4,rowspan=1)
Label(tablero,image=p8).grid(row=23, column=5,rowspan=1)
Label(tablero,image=p1).grid(row=22, column=2,rowspan=1,pady=10)
Label(tablero,image=p2).grid(row=22, column=3,rowspan=1,pady=10)
Label(tablero,image=p3).grid(row=22, column=4,rowspan=1,pady=10)
Label(tablero,image=p4).grid(row=22, column=5,rowspan=1,pady=10)
#test vacio
Label(tablero,image=pv).grid(row=20,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=20,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=20,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=20,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=18,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=18,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=18,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=18,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=16,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=16,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=16,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=16,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=14,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=14,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=14,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=14,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=12,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=12,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=12,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=12,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=10,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=10,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=10,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=10,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=8,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=8,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=8,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=8,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=6,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=6,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=6,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=6,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=4,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=4,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=4,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=4,column=5,rowspan=2)
Label(tablero,image=pv).grid(row=2,column=2,rowspan=2)
Label(tablero,image=pv).grid(row=2,column=3,rowspan=2)
Label(tablero,image=pv).grid(row=2,column=4,rowspan=2)
Label(tablero,image=pv).grid(row=2,column=5,rowspan=2)
Label(tablero,image=pres).grid(row=0,column=2,rowspan=2)
Label(tablero,image=pres).grid(row=0,column=3,rowspan=2)
Label(tablero,image=pres).grid(row=0,column=4,rowspan=2)
Label(tablero,image=pres).grid(row=0,column=5,rowspan=2)
#checks vacios
Label(tablero,image=checkv).grid(row=21,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=21,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=20,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=20,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=19,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=19,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=18,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=18,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=17,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=17,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=16,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=16,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=15,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=15,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=14,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=14,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=13,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=13,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=12,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=12,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=11,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=11,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=10,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=10,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=9,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=9,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=8,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=8,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=7,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=7,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=6,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=6,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=5,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=5,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=4,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=4,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=3,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=3,column=8,rowspan=1)
Label(tablero,image=checkv).grid(row=2,column=7,rowspan=1)
Label(tablero,image=checkv).grid(row=2,column=8,rowspan=1)

def sup():
    #test vacio
    Label(tablero,image=pv).grid(row=20,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=20,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=20,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=20,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=18,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=18,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=18,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=18,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=16,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=16,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=16,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=16,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=14,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=14,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=14,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=14,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=12,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=12,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=12,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=12,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=10,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=10,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=10,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=10,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=8,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=8,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=8,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=8,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=6,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=6,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=6,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=6,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=4,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=4,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=4,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=4,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=2,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=2,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=2,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=2,column=5,rowspan=2)
    Label(tablero,image=pres).grid(row=0,column=2,rowspan=2)
    Label(tablero,image=pres).grid(row=0,column=3,rowspan=2)
    Label(tablero,image=pres).grid(row=0,column=4,rowspan=2)
    Label(tablero,image=pres).grid(row=0,column=5,rowspan=2)
    #checks vacios
    Label(tablero,image=checkv).grid(row=21,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=21,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=20,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=20,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=19,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=19,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=18,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=18,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=17,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=17,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=16,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=16,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=15,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=15,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=14,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=14,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=13,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=13,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=12,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=12,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=11,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=11,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=10,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=10,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=9,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=9,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=8,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=8,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=7,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=7,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=6,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=6,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=5,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=5,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=4,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=4,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=3,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=3,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=2,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=2,column=8,rowspan=1)

def star():
    #test vacio
    Label(tablero,image=pv).grid(row=20,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=20,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=20,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=20,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=18,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=18,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=18,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=18,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=16,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=16,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=16,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=16,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=14,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=14,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=14,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=14,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=12,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=12,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=12,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=12,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=10,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=10,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=10,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=10,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=8,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=8,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=8,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=8,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=6,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=6,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=6,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=6,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=4,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=4,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=4,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=4,column=5,rowspan=2)
    Label(tablero,image=pv).grid(row=2,column=2,rowspan=2)
    Label(tablero,image=pv).grid(row=2,column=3,rowspan=2)
    Label(tablero,image=pv).grid(row=2,column=4,rowspan=2)
    Label(tablero,image=pv).grid(row=2,column=5,rowspan=2)
    Label(tablero,image=pres).grid(row=0,column=2,rowspan=2)
    Label(tablero,image=pres).grid(row=0,column=3,rowspan=2)
    Label(tablero,image=pres).grid(row=0,column=4,rowspan=2)
    Label(tablero,image=pres).grid(row=0,column=5,rowspan=2)
    #checks vacios
    Label(tablero,image=checkv).grid(row=21,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=21,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=20,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=20,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=19,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=19,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=18,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=18,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=17,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=17,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=16,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=16,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=15,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=15,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=14,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=14,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=13,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=13,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=12,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=12,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=11,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=11,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=10,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=10,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=9,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=9,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=8,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=8,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=7,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=7,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=6,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=6,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=5,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=5,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=4,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=4,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=3,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=3,column=8,rowspan=1)
    Label(tablero,image=checkv).grid(row=2,column=7,rowspan=1)
    Label(tablero,image=checkv).grid(row=2,column=8,rowspan=1)
    print("nuevo")
    #parametros
    B=[]
    P=[]
    F1=[]
    F2=[]
    F3=[]
    F4=[]
    posm=[]
    #check
    c1=0
    c2=0
    c3=0
    c4=0
    gam=1
    inte=1
    #parametros

    re1=0
    re2=0
    re3=0
    
    a=0
    #bucle para darle valores aleatorios a la respuesta y el primer intento
    while a<4:
       B.append(random.randint(0, 7))
       P.append(random.randint(0, 7))
       a=a+1
    
    ##primera prueba
    

    #mostrar respuesta
    if B[0]==0:
        Label(tablero,image=p1).grid(row=0,column=2,rowspan=2)
    elif B[0]==1:
        Label(tablero,image=p2).grid(row=0,column=2,rowspan=2)
    elif B[0]==2:
        Label(tablero,image=p3).grid(row=0,column=2,rowspan=2)
    elif B[0]==3:
        Label(tablero,image=p4).grid(row=0,column=2,rowspan=2)
    elif B[0]==4:
        Label(tablero,image=p5).grid(row=0,column=2,rowspan=2)
    elif B[0]==5:
        Label(tablero,image=p6).grid(row=0,column=2,rowspan=2)
    elif B[0]==6:
        Label(tablero,image=p7).grid(row=0,column=2,rowspan=2)
    elif B[0]==7:
        Label(tablero,image=p8).grid(row=0,column=2,rowspan=2)
    if B[1]==0:
        Label(tablero,image=p1).grid(row=0,column=3,rowspan=2)
    elif B[1]==1:
        Label(tablero,image=p2).grid(row=0,column=3,rowspan=2)
    elif B[1]==2:
        Label(tablero,image=p3).grid(row=0,column=3,rowspan=2)
    elif B[1]==3:
        Label(tablero,image=p4).grid(row=0,column=3,rowspan=2)
    elif B[1]==4:
        Label(tablero,image=p5).grid(row=0,column=3,rowspan=2)
    elif B[1]==5:
        Label(tablero,image=p6).grid(row=0,column=3,rowspan=2)
    elif B[1]==6:
        Label(tablero,image=p7).grid(row=0,column=3,rowspan=2)
    elif B[1]==7:
        Label(tablero,image=p8).grid(row=0,column=3,rowspan=2)
    if B[2]==0:
        Label(tablero,image=p1).grid(row=0,column=4,rowspan=2)
    elif B[2]==1:
        Label(tablero,image=p2).grid(row=0,column=4,rowspan=2)
    elif B[2]==2:
        Label(tablero,image=p3).grid(row=0,column=4,rowspan=2)
    elif B[2]==3:
        Label(tablero,image=p4).grid(row=0,column=4,rowspan=2)
    elif B[2]==4:
        Label(tablero,image=p5).grid(row=0,column=4,rowspan=2)
    elif B[2]==5:
        Label(tablero,image=p6).grid(row=0,column=4,rowspan=2)
    elif B[2]==6:
        Label(tablero,image=p7).grid(row=0,column=4,rowspan=2)
    elif B[2]==7:
        Label(tablero,image=p8).grid(row=0,column=4,rowspan=2)
    if B[3]==0:
        Label(tablero,image=p1).grid(row=0,column=5,rowspan=2)
    elif B[3]==1:
        Label(tablero,image=p2).grid(row=0,column=5,rowspan=2)
    elif B[3]==2:
        Label(tablero,image=p3).grid(row=0,column=5,rowspan=2)
    elif B[3]==3:
        Label(tablero,image=p4).grid(row=0,column=5,rowspan=2)
    elif B[3]==4:
        Label(tablero,image=p5).grid(row=0,column=5,rowspan=2)
    elif B[3]==5:
        Label(tablero,image=p6).grid(row=0,column=5,rowspan=2)
    elif B[3]==6:
        Label(tablero,image=p7).grid(row=0,column=5,rowspan=2)
    elif B[3]==7:
        Label(tablero,image=p8).grid(row=0,column=5,rowspan=2)
    print(B)
    
#repetidos
    con=0
    #bucle para los intentos
    while con==0:
        #repeticiones
        if P[0]==P[1]:
            re1=re1+1
        if P[0]==P[2]:
            re1=re1+1
        if P[0]==P[3]:
            re1=re1+1
        if P[0]!=P[1]:
            if P[1]==P[2]:
                re2=re2+1
            if P[1]==P[3]:
                re2=re2+1
        if P[1]!=P[2]:
            if P[2]==P[3]:
                re3=re3+1
        #chequeo
        #1 bien,2 posible
        for i in range(len(B)):
            if P[0]==B[i]:
                if i==0:
                    c1=1
                else:
                    if c1!=1:
                        c1=2
            elif c1!=2 and c1!=1:
                c1=3
            if P[1]==B[i]:
                if i==1:
                    c2=1
                else:
                    if c2!=1:
                        c2=2
            elif c2!=2 and c2!=1:
                c2=3
            if P[2]==B[i]:
                if i==2:
                    c3=1
                else:
                    if c3!=1:
                        c3=2
            elif c3!=2 and c3!=1:
                c3=3
            if P[3]==B[i]:
                if i==3:
                    c4=1
                else:
                    if c4!=1:
                        c4=2
            elif c4!=2 and c4!=1:
                c4=3
        
        reps=0
        for i in range(len(B)):
            if re1>=1:
                for q in range(len(B)):
                    if P[0]==B[q]:
                        reps=reps+1
                if reps<re1:
                    if P[0]==P[1]:
                        if c1<c2:
                            if c2!=1:
                                c2=3
                        else:
                            if c1!=1:
                                c1=3
                    if P[0]==P[2]:
                        if c1<c3:
                            if c3!=1:
                                c3=3
                        else:
                            if c1!=1:
                                c1=3
                    if P[0]==P[3]:
                        if c1<c4:
                            if c4!=1:
                                c4=3
                        else:
                            if c1!=1:
                                c1=3
            reps=0
            if re2>=1 or P[0]==P[1]:
                for q in range(len(B)):
                    if P[1]==B[q]:
                        reps=reps+1
                if reps<re2:
                    if P[1]==P[2]:
                        if c2<c3:
                            if c3!=1:
                                c3=3
                        else:
                            if c2!=1:
                                c2=3
                    elif P[1]==P[3]:
                        if c2<c4:
                            if c4!=1:
                                c4=3
                        else:
                            if c2!=1:
                                c2=3
            reps=0
            if re3>=1 or P[1]==P[2]:
                for q in range(len(B)):
                    if P[2]==B[q]:
                        reps=reps+1
                if reps<re3:
                    if P[2]==P[3]:
                        if c3<c4:
                            if c4!=1:
                                c4=3
                        else:
                            if c3!=1:
                                c3=3
                            
        if c1==3 or c1==2:
            F1.append(P[0])
    
        if c2==3 or c2==2:
            F2.append(P[1])
            
        if c3==3 or c3==2:
            F3.append(P[2])
    
        if c4==3 or c4==2:
            F4.append(P[3])
            
        print(P)        
        print(c1,c2,c3,c4)
        z=c1+c2+c3+c4
        if z!=4:
            if c1!=1:
                r=0
                while r==0:
                    cont=0
                    P1=random.randint(0, 7)
                    for i in range(len(F1)):
                        if P1==F1[i]:
                            cont=cont+1
                    if cont<1:
                        r=1
                    if cont==8:
                        r=1
                P[0]=P1
            
            if c2!=1:
                r=0
                while r==0:
                    cont=0
                    P2=random.randint(0, 7)
                    for i in range(len(F2)):
                        if P2==F2[i]:
                            cont=cont+1
                    if cont<1:
                        r=1
                    if cont==8:
                        r=1
                P[1]=P2
                
            if c3!=1:
                r=0
                while r==0:
                    cont=0
                    P3=random.randint(0, 7)
                    for i in range(len(F3)):
                        if P3==F3[i]:
                            cont=cont+1
                    if cont<1:
                        r=1
                    if cont==8:
                        r=1
                P[2]=P3
                
            if c4!=1:
                r=0
                while r==0:
                    cont=0
                    P4=random.randint(0, 7)
                    for i in range(len(F4)):
                        if P4==F4[i]:
                            cont=cont+1
                    if cont<1:
                        r=1
                    if cont==8:
                        r=1
                P[3]=P4
        
        print("intento",inte)
        
        #mostrador
        if z!=4:
            if inte==1:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=20,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=20,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=20,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=20,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=20,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=20,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=20,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=20,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=20,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=20,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=20,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=20,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=20,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=20,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=20,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=20,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=20,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=20,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=20,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=20,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=20,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=20,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=20,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=20,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=20,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=20,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=20,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=20,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=20,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=20,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=20,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=20,column=5,rowspan=2)
            elif inte==2:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=18,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=18,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=18,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=18,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=18,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=18,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=18,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=18,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=18,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=18,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=18,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=18,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=18,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=18,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=18,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=18,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=18,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=18,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=18,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=18,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=18,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=18,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=18,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=18,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=18,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=18,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=18,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=18,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=18,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=18,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=18,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=18,column=5,rowspan=2)
            elif inte==3:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=16,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=16,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=16,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=16,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=16,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=16,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=16,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=16,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=16,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=16,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=16,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=16,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=16,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=16,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=16,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=16,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=16,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=16,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=16,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=16,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=16,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=16,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=16,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=16,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=16,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=16,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=16,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=16,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=16,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=16,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=16,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=16,column=5,rowspan=2)
            elif inte==4:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=14,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=14,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=14,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=14,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=14,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=14,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=14,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=14,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=14,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=14,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=14,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=14,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=14,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=14,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=14,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=14,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=14,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=14,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=14,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=14,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=14,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=14,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=14,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=14,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=14,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=14,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=14,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=14,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=14,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=14,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=14,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=14,column=5,rowspan=2)
            elif inte==5:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=12,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=12,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=12,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=12,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=12,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=12,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=12,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=12,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=12,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=12,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=12,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=12,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=12,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=12,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=12,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=12,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=12,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=12,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=12,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=12,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=12,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=12,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=12,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=12,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=12,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=12,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=12,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=12,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=12,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=12,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=12,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=12,column=5,rowspan=2)
            elif inte==6:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=10,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=10,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=10,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=10,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=10,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=10,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=10,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=10,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=10,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=10,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=10,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=10,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=10,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=10,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=10,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=10,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=10,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=10,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=10,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=10,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=10,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=10,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=10,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=10,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=10,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=10,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=10,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=10,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=10,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=10,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=10,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=10,column=5,rowspan=2)
            elif inte==7:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=8,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=8,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=8,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=8,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=8,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=8,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=8,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=8,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=8,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=8,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=8,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=8,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=8,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=8,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=8,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=8,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=8,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=8,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=8,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=8,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=8,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=8,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=8,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=8,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=8,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=8,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=8,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=8,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=8,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=8,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=8,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=8,column=5,rowspan=2)
            elif inte==8:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=6,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=6,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=6,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=6,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=6,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=6,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=6,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=6,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=6,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=6,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=6,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=6,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=6,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=6,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=6,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=6,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=6,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=6,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=6,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=6,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=6,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=6,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=6,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=6,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=6,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=6,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=6,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=6,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=6,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=6,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=6,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=6,column=5,rowspan=2)
            elif inte==9:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=4,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=4,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=4,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=4,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=4,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=4,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=4,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=4,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=4,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=4,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=4,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=4,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=4,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=4,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=4,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=4,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=4,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=4,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=4,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=4,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=4,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=4,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=4,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=4,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=4,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=4,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=4,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=4,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=4,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=4,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=4,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=4,column=5,rowspan=2)
            elif inte==10:
                if P[0]==0:
                    Label(tablero,image=p1).grid(row=2,column=2,rowspan=2)
                elif P[0]==1:
                    Label(tablero,image=p2).grid(row=2,column=2,rowspan=2)
                elif P[0]==2:
                    Label(tablero,image=p3).grid(row=2,column=2,rowspan=2)
                elif P[0]==3:
                    Label(tablero,image=p4).grid(row=2,column=2,rowspan=2)
                elif P[0]==4:
                    Label(tablero,image=p5).grid(row=2,column=2,rowspan=2)
                elif P[0]==5:
                    Label(tablero,image=p6).grid(row=2,column=2,rowspan=2)
                elif P[0]==6:
                    Label(tablero,image=p7).grid(row=2,column=2,rowspan=2)
                elif P[0]==7:
                    Label(tablero,image=p8).grid(row=2,column=2,rowspan=2)
                if P[1]==0:
                    Label(tablero,image=p1).grid(row=2,column=3,rowspan=2)
                elif P[1]==1:
                    Label(tablero,image=p2).grid(row=2,column=3,rowspan=2)
                elif P[1]==2:
                    Label(tablero,image=p3).grid(row=2,column=3,rowspan=2)
                elif P[1]==3:
                    Label(tablero,image=p4).grid(row=2,column=3,rowspan=2)
                elif P[1]==4:
                    Label(tablero,image=p5).grid(row=2,column=3,rowspan=2)
                elif P[1]==5:
                    Label(tablero,image=p6).grid(row=2,column=3,rowspan=2)
                elif P[1]==6:
                    Label(tablero,image=p7).grid(row=2,column=3,rowspan=2)
                elif P[1]==7:
                    Label(tablero,image=p8).grid(row=2,column=3,rowspan=2)
                if P[2]==0:
                    Label(tablero,image=p1).grid(row=2,column=4,rowspan=2)
                elif P[2]==1:
                    Label(tablero,image=p2).grid(row=2,column=4,rowspan=2)
                elif P[2]==2:
                    Label(tablero,image=p3).grid(row=2,column=4,rowspan=2)
                elif P[2]==3:
                    Label(tablero,image=p4).grid(row=2,column=4,rowspan=2)
                elif P[2]==4:
                    Label(tablero,image=p5).grid(row=2,column=4,rowspan=2)
                elif P[2]==5:
                    Label(tablero,image=p6).grid(row=2,column=4,rowspan=2)
                elif P[2]==6:
                    Label(tablero,image=p7).grid(row=2,column=4,rowspan=2)
                elif P[2]==7:
                    Label(tablero,image=p8).grid(row=2,column=4,rowspan=2)
                if P[3]==0:
                    Label(tablero,image=p1).grid(row=2,column=5,rowspan=2)
                elif P[3]==1:
                    Label(tablero,image=p2).grid(row=2,column=5,rowspan=2)
                elif P[3]==2:
                    Label(tablero,image=p3).grid(row=2,column=5,rowspan=2)
                elif P[3]==3:
                    Label(tablero,image=p4).grid(row=2,column=5,rowspan=2)
                elif P[3]==4:
                    Label(tablero,image=p5).grid(row=2,column=5,rowspan=2)
                elif P[3]==5:
                    Label(tablero,image=p6).grid(row=2,column=5,rowspan=2)
                elif P[3]==6:
                    Label(tablero,image=p7).grid(row=2,column=5,rowspan=2)
                elif P[3]==7:
                    Label(tablero,image=p8).grid(row=2,column=5,rowspan=2)
        
        
        if inte==2:
            if c1==1:
                Label(tablero,image=check1).grid(row=20,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=20,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=20,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=20,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=20,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=20,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=21,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=21,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=21,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=21,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=21,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=21,column=8,rowspan=1)
        if inte==3:
            if c1==1:
                Label(tablero,image=check1).grid(row=18,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=18,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=18,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=18,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=18,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=18,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=19,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=19,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=19,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=19,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=19,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=19,column=8,rowspan=1)
        if inte==4:
            if c1==1:
                Label(tablero,image=check1).grid(row=16,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=16,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=16,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=16,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=16,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=16,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=17,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=17,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=17,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=17,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=17,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=17,column=8,rowspan=1)
        if inte==5:
            if c1==1:
                Label(tablero,image=check1).grid(row=14,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=14,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=14,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=14,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=14,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=14,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=15,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=15,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=15,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=15,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=15,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=15,column=8,rowspan=1)
        if inte==6:
            if c1==1:
                Label(tablero,image=check1).grid(row=12,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=12,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=12,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=12,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=12,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=12,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=13,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=13,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=13,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=13,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=13,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=13,column=8,rowspan=1)
        if inte==7:
            if c1==1:
                Label(tablero,image=check1).grid(row=10,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=10,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=10,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=10,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=10,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=10,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=9,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=9,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=9,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=9,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=9,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=9,column=8,rowspan=1)
        if inte==8:
            if c1==1:
                Label(tablero,image=check1).grid(row=8,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=8,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=8,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=8,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=8,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=8,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=9,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=9,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=9,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=9,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=9,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=9,column=8,rowspan=1)
        if inte==9:
            if c1==1:
                Label(tablero,image=check1).grid(row=6,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=6,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=6,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=6,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=6,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=6,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=7,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=7,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=7,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=7,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=7,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=7,column=8,rowspan=1)
        if inte==10:
            if c1==1:
                Label(tablero,image=check1).grid(row=4,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=4,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=4,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=4,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=4,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=4,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=5,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=5,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=5,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=5,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=5,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=5,column=8,rowspan=1)
        if inte==11:
            if c1==1:
                Label(tablero,image=check1).grid(row=2,column=7,rowspan=1)
            if c1==2:
                Label(tablero,image=check2).grid(row=2,column=7,rowspan=1)
            if c1==3:
                Label(tablero,image=check3).grid(row=2,column=7,rowspan=1)
            if c2==1:
                Label(tablero,image=check1).grid(row=2,column=8,rowspan=1)
            if c2==2:
                Label(tablero,image=check2).grid(row=2,column=8,rowspan=1)
            if c2==3:
                Label(tablero,image=check3).grid(row=2,column=8,rowspan=1)
            if c3==1:
                Label(tablero,image=check1).grid(row=3,column=7,rowspan=1)
            if c3==2:
                Label(tablero,image=check2).grid(row=3,column=7,rowspan=1)
            if c3==3:
                Label(tablero,image=check3).grid(row=3,column=7,rowspan=1)
            if c4==1:
                Label(tablero,image=check1).grid(row=3,column=8,rowspan=1)
            if c4==2:
                Label(tablero,image=check2).grid(row=3,column=8,rowspan=1)
            if c4==3:
                Label(tablero,image=check3).grid(row=3,column=8,rowspan=1)
        
        if z==4:
            print("gano")
            print(B)
            print(P)
            con=1
        else:
            inte=inte+1
        
        if inte==10:
            con=1
    
    

    
ventana.mainloop()
