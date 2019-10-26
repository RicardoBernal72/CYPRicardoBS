N=int(input("numero de Datos enteros:"))
SUMPOS=0
SUMTR=0
CUEPOS=0
PROPOS=0
PROGEN=0
I=1
for I in range(0,N,1):
    if N>=1:
        NUM=int(input("DAME un numero: "))
        if NUM>0:
            SUMPOS=(NUM+SUMPOS)
            CUEPOS+=1
        else:
            SUMTR=(NUM+SUMTR)
    else:
        PROGEN=(SUMPOS+SUMTR)/N
        PROPOS=(SUMPOS/CUEPOS)
        I=I+1
print(CUEPOS)
print(PROPOS)
print(PROGEN)
            
