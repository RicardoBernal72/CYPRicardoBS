CAL1=float(input("primer calificacion: "))
CAL2=float(input("segunda calificacion: "))
CAL3=float(input("tercer calificacion: "))
CAL4=float(input("cuarta calificacion: "))
CAL5=float(input("quinta calificacion: "))
PRO=(CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
if PRO>=6:
    print(f"Bien aventurado sea usted ha pasado la materia con un promedio de {PRO} ")
else:
    print(f"UFFF, no ha pasado la materia puesto que su promedio ha sido de {PRO}  ")


