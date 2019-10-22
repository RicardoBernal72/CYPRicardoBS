ARSU=0
ARNO=0
ARCE=0
MERSU=50000
MES=0
for I in range(1,13,1):
    print(f"MES {I}:")
    RNO=int(input("promedio de lluvias del mes:"))
    RCE=int(input("promedio de lluvias del mes:"))
    RSU=int(input("promedio de lluvias del mes:"))

    ARNO = ARNO+RNO
    ARCE = ARCE+RCE
    ARSU = ARSU+RSU

    if RSU < MERSU: #aqui termina el for
        MERSU = RSU
        MES = I
PROCE = ARCE/12
print(f"el promedio de lluvias es {PROCE}")
print(f"mes con menor lluvia en el sur {MES}")
print(f"REgistro del mes con menor lluvia es {MERSU}")

if ARNO > ARCE:
    if ARNO > ARSU:
        print("la region con mayor lluvia es la norte")
    else:
        print("la region con mayor lluvia es la sur")

elif ARCE > ARSU:
    print("la regin con mayores lluvias es la region centro")
else:
    print("la region con mayores lluvias es la sur")
    
