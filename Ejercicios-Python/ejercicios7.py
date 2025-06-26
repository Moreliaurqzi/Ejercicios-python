sumapost = 0
sumaneg = 0
i = 0
while i < 100:
 num=int(input("Ingrese un numero"))
 if num > 0:
    sumapost+=num
 else:
    sumaneg+=num
 i+=1
 print(sumapost,sumaneg) 
 
 
 
 #ejercicio 8 while
 positivos = 0
 negativos = 0
 nulos = 0
 i = 0
 while i < 5:
  num=int(input("Ingrese un numero"))
if num > 0:
    positivos +=1
elif num < 0:
    negativos +=1
else:
    nulos +=1
    i+=1
print("cantidad de positivos", positivos)
print("cantidad de negativos", negativos)
print("cantidad de nulos", nulos)


#ejercicio 8 for
positivos = 0
negativos = 0
nulos = 0
for i in range(0,5):
    N=float(input("ingrese en un numero:"))
if N>0 :
    positivos=positivos+1
elif N<0:
    negativos=negativos+1
else:
    nulos=nulos+1
print("la cantidad de numeros positivos es:", positivos)
print("la cantidad de numeros negativos es:", negativos)
print("la cantidad de numeros nulos es:", nulos)


#ejercicio 10 while
suma=0
positivo=0
nulos=0
while i < 5:
    N=int(input("ingrese un numero:  "))
if N>0:
    suma=suma+N
elif N<0:
    positivo=positivo+N
else:
    nulos=nulos+1
    




#ejercicio 11 while
pares=0
impares=0
i=0
while i < 100:
 num=int(input("ingrese un numero"))
if num > 0:
  pares+=num
else:
    impares+=num
print("la suma de los numeros pares es:", pares)
print("la suma de los numeros impares:", impares)

#ejercicio 14






#ejercicio 15 while
cont=20
suma=0
while cont >0:
    nro=int(input("ingrese un nro"))
    suma+=nro
    cont=-1
print("la suma es:", suma)


#ejercicio 18 while
suma=0
i=0
a=int(input("ingrese un numero"))
b=int(input("ingrese un numero"))







#ejercicio 19
i=1
may=N
while i < 100:
 N=int(input("ingrese un numero"))
 if  N>may:
     may=N
     i=i+1
print(may)



#ejercicio 20
i=1
may=N
men=N
while i < 100:
  n=int(input("ingrese un numero"))
if n>may:
    may=N
elif n<men:
    men=N
i+=1
print(may, men)

#ejercicio 21
mayor=0
menor=0
suma=0
prom=0
entre=0
men12=0
nombre_del_menor=0
nombre=(str(input("ingrese el nombre:  ")))
edad=int(input("ingrese la edad"))
mayor=edad
menor=edad
suma=edad
if edad <12:
    men12=men12+1
if 10<=edad<=16:
    entre=entre+1
print("el ") 