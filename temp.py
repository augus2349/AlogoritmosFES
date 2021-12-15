a=int(input("numero de varibeles minimo 4, maximo 10 "))
if a>10 or a<4:
    print("error al seleccionar varibles") 
else:
    b=input("introudusca los miniterminos (ej. 2 5 7) ")
    t=[]
    t=b.split()

x=0
m1=[]
m2=[]
m3=[]
m4=[]
m5=[]
m6=[]
m7=[]
m8=[]
m9=[]
m10=[]
m=[]
u=[]
mx=[]
m1m2=[]
m2m3=[]
m3m4=[]
m4m5=[]
m5m6=[]
m6m7=[]
m7m8=[]
m8m9=[]
m9m10=[]
s=[0,0,0,0]



def calcula_terminos(): 
    i=0
    for x in t:
        n=int(x)
        #definir los valores del minitermino
        if n==0:
            for i in range(4):
                m.append(0)
        else:
            while n != 0: 
                modulo = n % 2
                c = n // 2
                m.append(modulo)
                n = c
            while i < len(m):
              i = i + 1
            while i<a:
                m.append(0)
                i=i+1
        u=m[::-1]
        mx.append(u)
        m.clear()
        i=0 
    print(mx)

def separador():

    l=0
    for j in range(len(mx)):
        for k in range(len(mx[j])):
            if mx[j][k]==1:
                l=l+1
        if l==1:
            m1.append(mx[j])
            print(mx[j])
        elif l==2:
            m2.append(mx[j])
        elif l==3:
            m3.append(mx[j])
        elif l==4:
            m4.append(mx[j])
        elif l==5:
            m5.append(mx[j])
        elif l==6:
            m6.append(mx[j])
        elif l==7:
            m7.append(mx[j])
        elif l==8:
            m8.append(mx[j])
        elif l==9:
            m9.append(mx[j])
        elif l==10:
            m10.append(mx[j])
        l=0

def tablas():
    
    com=0
    pos_cam=0
    p=0
    #m1 con m2
    for q in range(len(m1)):
        for w in range(len(m2)):
            while p<4:
                if (m1[q][p]) == (m2[w][p]):
                    if p==0:
                        s1=int(m2[w][p])
                    elif p==1:
                        s2=int(m2[w][p])
                    elif p==2:
                        s3=int(m2[w][p])
                    elif p==3:
                        s4=int(m2[w][p])
                else:
                    com=com+1
                    pos_cam=p
                p=p+1
        
            if com==1:
                if pos_cam==0:
                    s1="-"
                elif pos_cam==1:
                    s2="-"
                elif pos_cam==2:
                    s3="-"
                elif pos_cam==3:
                    s4="-"
                m1m2.append([s1,s2,s3,s4])
            p=0
            com=0
    #m2 con m3
    for q in range(len(m2)):
        for w in range(len(m3)):
            while p<4:
                if (m2[q][p]) == (m3[w][p]):
                    if p==0:
                        s1=int(m3[w][p])
                    elif p==1:
                        s2=int(m3[w][p])
                    elif p==2:
                        s3=int(m3[w][p])
                    elif p==3:
                        s4=int(m3[w][p])
                else:
                    com=com+1
                    pos_cam=p
                p=p+1
                
            if com==1:
                if pos_cam==0:
                    s1="-"
                elif pos_cam==1:
                    s2="-"
                elif pos_cam==2:
                    s3="-"
                elif pos_cam==3:
                    s4="-"
                m2m3.append([s1,s2,s3,s4])
            p=0
            com=0
    #m3 a m4
    for q in range(len(m3)):
        for w in range(len(m4)):
            while p<4:
                if (m3[q][p]) == (m4[w][p]):
                    if p==0:
                        s1=int(m4[w][p])
                    elif p==1:
                        s2=int(m4[w][p])
                    elif p==2:
                        s3=int(m4[w][p]) 
                    elif p==3:
                        s4=int(m4[w][p])
                else:
                    com=com+1
                    pos_cam=p
                p=p+1
           
            if com==1:
                if pos_cam==0:
                    s1="-"
                elif pos_cam==1:
                    s2="-"
                elif pos_cam==2:
                    s3="-"
                elif pos_cam==3:
                    s4="-"
                m3m4.append([s1,s2,s3,s4])
            p=0
            com=0

#reductor segun las varibables
if a==4:
    print(1) 
    calcula_terminos()
    separador()
    print(m1,"1")
    print(m2,"2")
    print(m3,"3")
    print(m4,"4")
    tablas()
    m1=m1m2
    m2=m2m3
    m3=m3m4
    print(m1,"11")
    print(m2,"22")
    if m3==[]:    
        print("vacio")
    else:
        print(m3,"33")
elif a==5:
    print(2)
    calcula_terminos()
    separador()
elif a==6:
    print(3)
    calcula_terminos()
    separador()
elif a==7:
    print(4)
    calcula_terminos()
    separador()
elif a==8:
    print(5)
    calcula_terminos()
    separador()
elif a==9:
    print(6)
    calcula_terminos()
    separador()
elif a==10:
    print(7)
    calcula_terminos()
    separador()
    
    