archivo=open("numeros.txt","rt")
#print(dir(archivo))
numeros1=archivo.read()
print(numeros1)
print(numeros1.split('t'))
lista_num=[]
for linea in numeros1.split('t'):
    for numero in linea.split(','):
        lista_num.append(int(numero))
print(lista_num)
lista_num.sort()
print(f"la lista ord es:{lista_num}")
print(f"el menor de la lista es {lista_num[-1]}")
archivo.close

archivo=open("numeros.txt","rt")
numeros2=archivo.readlines()
print(numeros2)
archivo.close()

archivo=open("numeros.txt","rt")
numeros2=archivo.readline()
print(numeros2)
archivo.close()
