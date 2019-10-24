SERIE=0
N=int(input("numero de terminos de la serie:"))
I=1
BAND=True
for I in range(1,N,1):
    if BAND==True:
        SERIE=(SERIE+1)/I
        BAND=False
    else:
        SERIE=(SERIE-1)/I
        BAND=True
    I=I+1
print(SERIE)

