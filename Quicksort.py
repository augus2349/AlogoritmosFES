import numpy as np

def seleccionarPivote(X):
    indice =np.random.randint(0,len(X))
    return X[indice]

def dividirLista(X,pivote):
    mayores=[]
    menores=[]
    pivotes=[]
    for e in X:
        if (pivote==e):
            pivotes.append(e)
        else:
            if(pivote>e):
                menores.append(e)
            else:
                mayores.append(e)
    return mayores,menores,pivotes

def quicksort(X):
    pivote=seleccionarPivote(X)
    mayores,menores,pivotes = dividirLista(X,pivote)
    if(len(mayores)>=2 and not mayores==X):
        mayores=quicksort(mayores)
    if(len(menores)>=2and not menores==X):
        menores=quicksort(menores)
    return menores+pivotes+mayores

#a=[0,3,5,7,2,4,3,5]
a=[]
n=100000000
for i in range(n):
    a.append(np.random.randint(0,n))

print(a)
print("ordenando...")
print(quicksort(a))

ordenados=True
for i in range(n-1):
    if(a[i]>a[i]):
        ordenados=False

if(ordenados):
    print("si se ordenaron1")
else:
    print("no se ordenaron")