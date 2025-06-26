#Ejercicio de diagrama de flujo
A=int(input("Ingrese un numero"))
B=int(input("Ingrese otro numero"))
if A>B:
    print(A)
else:
    print(B)
    
    
    #Ejercicio n5
lados=input("Ingrese la cantidad de lados")
match lados:
    case "3":
        print("triangulo")
    case "4":
        print("cuadrilatero")
    case"5":
        print("pentagono")
    case _:
        print()
        
        
        
    #7
sumapost= 0
sumaneg=0
i=0
while i < 100:
 num=int(input("Ingrese un numero"))
if num > 0:
    sumapost+=num
else:
    sumaneg+=num
i+=1
print(sumapost, sumaneg)
    
    


        