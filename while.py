otra =  bool(int(input("hay mas alumnos?(0 NO, 1 si): " )))
Suma = 0.0
Cont=0
while(otra == True):
    Cal = float(input("calificacion:" ))
    Cont+=1
    Suma += Cal
    otra = bool(int(input("hay mas alumnos?(0 NO, 1 si): " )))
print("suma", Suma)
print("PROMEDIO:",Suma/Cont)
print("Fin del programa")
