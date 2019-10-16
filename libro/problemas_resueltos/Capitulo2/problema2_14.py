TENFE=int(input("tipo de enfermedad 1 a 4: "))
EDAD=int(input("edad del paciente: "))
DIAS=int(input("num de dias que se paso hospitalizado"))
if TENFE==1:
    COSTO=DIAS*25
if TENFE==2:
    COSTO=DIAS*16
if TENFE==3:
    COSTO=DIAS*20
if TENFE==4:
    COSTO=DIAS*32
if EDAD>=14 and EDAD<=22:
   TOTAL=COSTO*1.10
   print(f"el costo total aumneta por entrar en el rango de edad:")
   print(TOTAL)
else:
    print(f"el precio final es de {COSTO}")


