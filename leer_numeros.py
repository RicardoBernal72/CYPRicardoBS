archivo=open("numeros.txt","rt")
#print(dir(archivo))
numeros1=archivo.read()
print(numeros1)
print(numeros1.split('t'))
lista_num=[]
for linea in numeros1.split('\n'):
    for numero in linea.split(','):
        lista_num.append(str(numero))
print(lista_num)
lista_num.sort()
print(f"la lista ord es:{lista_num}")
print(f"el menor de la lista es {lista_num[-1]}")
archivo.close()

archivo=open("numeros.txt","rt")
numerose=archivo.readlines()
lista_nu=[]
for linea in numerose.split('\n'):
    for numero in linea.split(','):
        print("mira empieza aqui_-------",numeros2)
archivo.close()

archivo=open("numeros.txt","rt")
numeros2=archivo.readline()
print(numeros2)
archivo.close()
