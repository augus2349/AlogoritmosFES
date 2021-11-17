a=int(input("numero de varibeles minimo 4, maximo 10 "))
if a>10 or a<4:
    print("error al seleccionar varibles") 
else:
    b=input("introudusca los miniterminos (ej. 2 5 7) ")
    t=[]
    t=b.split()

com=0
pos_cam=0
v=["A","B","C","D","E","F","G","H","I","J"]
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

#reductor segun las varibables
if a==4:
    print(1) 
    calcula_terminos()
    separador()
    
    if (m1[0][0]) != (m2[0][0]):
        com=com+1
        pos_cam=0
    if (m1[0][1]) != (m2[0][1]):
        com=com+1
        pos_cam=1
    if (m1[0][2]) != (m2[0][2]):
        com=com+1
        pos_cam=2
    if (m1[0][3]) != (m2[0][3]):
        com=com+1
        pos_cam=3
    if com==1:
        print("valido")
        
    print(m1,"1")
    print(m2,"2")
    print(m3,"3")
    print(m4,"4")
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
    
    