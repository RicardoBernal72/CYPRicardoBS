MAT=int(input("Matricula: "))
CARR=str(input("CARRERA: "))
SEM=int(input("Semestre: "))
PROM=float(input("promedio: "))
if CARR==ECONOMIA:
    if SEM>=6 and  PROM>=8.8:
        print(MAT)
        print("USTED HA SIDO ACEPTADO EN LA CARRERA DE {CARR}")
    else:
        print("IM so sorry")
if CARR==CONTABILIDAD:
    if SEM>=5 and  PROM>=8.5:
        print(MAT)
        print("USTED HA SIDO ACEPTADO EN LA CARRERA DE {CARR}")
    else:
        print("IM so sorry")
if CARR==COMPUTACION:
    if SEM>=6 and  PROM>=8.5:
        print(MAT)
        print("USTED HA SIDO ACEPTADO EN LA CARRERA DE {CARR}")
    else:
        print("IM so sorry")
if CARR==ADMINISTRACION:
    if SEM>=5 and  PROM>=8.5:
        print(MAT)
        print("USTED HA SIDO ACEPTADO EN LA CARRERA DE {CARR}")
    else:
        print("IM so sorry")
