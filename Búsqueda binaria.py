
n=1000
lista=[]
for i in range(n):
    lista.append(i)
    
def BB(lista,elemB):
    n=len(lista)
    if(lista[0]<=elemB and elemB<=lista[n-1]and not n==0):
        if(elemB==lista[int(n/2)]):
            print("Se encotro el elemento en la lista")
        else:
            if(elemB<lista[int(n/2)]):
                BB(lista[0:int(n/2)],elemB)
            else:
                BB(lista[int(n/2):n],elemB)
    else:
        print("el elemento no fue encontrado")