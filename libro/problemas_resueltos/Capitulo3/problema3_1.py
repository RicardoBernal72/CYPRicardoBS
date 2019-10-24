NUM=int(input("dame un numero entero: "))
SUMAPAR=0
SUMMP=0
CUEPAR=0
I=1
for I in range(1,10,1):
    NUM=int(input("dame un numero entero: "))
    if NUM>0:
        NUM=(-1)**NUM
        if NUM>0:
           SUMAPAR=SUMAPAR+NUM
           CUEPAR=CUEPAR+1
        else:
             SUMMP=SUMMP+NUM
    else:
        I=I+1
PROPAR=SUMAPAR/CUEPAR
print(PROPAR)
print(CUEPAR)
print(SUMMP)
print(SUMAPAR)
        
