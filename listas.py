# listas
lluvias_norte=[80,60,120,100,70,150,100,47,95,70,100,130]
for indice in range(0,12,1):
    print(f"mes {indice+1 } en region norte={lluvias_norte[indice]}")
print(lluvias_norte[4])
print(lluvias_norte[:5:])

SUELDOS=[]
suma=0
for indice in range(7):
    SUELDOS.append(int(input("sueldo")))

print(SUELDOS)

for indice in range(7):
    suma+=SUELDOS[indice]
promedio=suma/7
cont=0
for indice in range(7):
   if SUELDOS[indice]>promedio:
    cont+=1
    print(f"mayores: {SUELDOS[indice]}")
