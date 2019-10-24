NOM=0
SUE=float(input("Sueldo del trabajador"))
while (SUE>-1):
    if SUE<1000:
        NSUE=SUE*1.15
    else:
        NSUE=SUE*1.12
    NOM=NOM+NSUE
    print(NSUE)
    print(NOM)
    SUE=float(input("Sueldo del trabajador"))
if SUE<=-1:
    print(NOM)


