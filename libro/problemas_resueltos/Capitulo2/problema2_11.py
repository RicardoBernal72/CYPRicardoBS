CLAVE=int(input("Clave de la zona geografica: "))
NUMIN=int(input("Duracion de la llamada: "))
if CLAVE==12:
    Costo=NUMIN*2
if CLAVE==15:
    Costo=NUMIN*2.2
if CLAVE==18:
    Costo=NUMIN*4.5
if CLAVE==19:
    Costo=NUMIN*3.5
if CLAVE==23 or 25:
    Costo=NUMIN*6
if CLAVE==29:
    Costo=NUMIN*5
print(f"el costo de la llamda es de {Costo} ")
