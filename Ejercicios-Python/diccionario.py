#diccionario ejercicio 1

#archivo=open("words.txt") 
#diccionario=dict()
#for linea in archivo:
    #for palabra in linea.split():
        #if not palabra in diccionario:
           # diccionario[palabra]=1
        #else:
            #diccionario[palabra]+=1
#print(diccionario)


#ejercicion2
archivo=open("words.txt")
diccionario2=dict()
for linea in archivo:
    for palabra in linea.split():
        for letra in palabra:
            letra=letra.lower()
            if letra not in diccionario2:
                diccionario2[letra]=1
            else:
                diccionario2[letra]+=1
print(diccionario2)





#que lea solamente el (abc, eje 4
archivo=open("words.txt")
diccionario2=dict()
for linea in archivo:
    for palabra in linea.split():
        diccionario2[palabra]=diccionario2.get(palabra,0)+1
print(diccionario2)
b=True
for par in diccionario2:
    if b:
        mayorV=diccionario2[par]
        mayorC=par
        b=False
    else:
        if diccionario2[par]>mayorV:
            mayorV=diccionario2[par]
            mayorC=par
print(mayorC,mayorV)






#Ejercicio 4


