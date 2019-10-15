Monto=float(input("monto total:  "))
if Monto<500:
    print("NO hay descuento")
if Monto<1000 and Monto>=500:
    NM=Monto*.95
    print(NM)
if Monto<7000 and Monto>=1000:
    NM=Monto*.89
    print(NM)
if Monto<15000 and Monto>=7000:
    NM=Monto*.82
    print(NM)
if Monto>15000:
    NM=Monto*.75
    print(NM)

