#arreglos
# lectura
# escritura / asignacion
#actualizacion : insercion, eliminicion, modificacion,
#ordenamiento
# busqueda

#escritura
frutas= ["Zapote","Manzana","Pera","Aguacate","Durazno","Uva","Sandia"]
# lectura, el selector [indice
print(frutas[2])
#lectura con for
#for opcion 1
for indice in range(0,7,1):
    print(frutas[indice])
print("__----------------------")
#for opcion 2 -- popr un iterador for each
# es lo mismo que lo de arriba, pero mas varato

for fr in frutas:
    print(fr)

#asignacion
frutas[2]="Melon"
print(frutas)
#agrgar un elemento al final con .append("")

frutas.append("Naranja")
print(frutas)
print(len(frutas))
print("-----------------")
#mas info en el shell de python : dir(list), y para mas info help(list.ask)
frutas.insert(2,"limon")
print(frutas)
print(len(frutas))
frutas.insert(0,"Mamey")
#eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas.append("limon")
frutas.append("limon")
print(frutas)
frutas.remove("limon")
print(frutas)

#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)


#busqueda
print(f"el limon esta en la posicion .{ frutas.index('limon')}")
print(f"el limon esta{frutas.count('limon')} vces en la lista")
#concatenar
print(frutas)
otras_frutas = ["Rambutan","Nispero","liche","pitaya"]
frutas.extend(otras_frutas)
print(frutas)
#copia

otra_copia=frutas.copy()
otra_copia.append("fresa")
otra_copia.append("fresa")
print(frutas)
print(otra_copia)

