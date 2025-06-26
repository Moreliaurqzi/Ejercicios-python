
archivo= open("archivos/romeo.txt")
b=True
for linea in archivo:
    print(linea)
    if b:
       lista=lista.split()
       b=False
    else:
        for palabra in linea.split():
            if not palabra in lista:
                lista.append(palabra)
print(lista)




archivo=open("archivo/roemo.txt")
lista=list()
for linea in archivo:
    for palabra in linea.split():
        if not palabra in lista:
            lista.append(palabra)
print(lista)